from youtube_transcript_api import YouTubeTranscriptApi,TranscriptsDisabled
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")
video_id = 'E3oG313_kps'

try:
    transcript_text = YouTubeTranscriptApi.get_transcript(video_id=video_id,languages=['hi',"en"])
    text = " ".join([i['text'] for i in transcript_text])

except TranscriptsDisabled:
    print("No captions available for this video")

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,chunk_overlap=100
)

chunks = text_splitter.create_documents(texts=[text])

embedd = HuggingFaceEmbeddings()
db = FAISS.from_documents(chunks,embedd)

retriver = db.as_retriever(search_type = "similarity",kwargs={"k":3})

prompt = PromptTemplate(
    template= '''You are a helpful AI assistant.
    Answer from the following context. 
    if context is insufficient, just say, I don't Know.
    if anyone ask the quesion in english, then answer in Englsih.
    context: {context}
    Question: {question}''',
    input_variables=["context","question"]
    )

question = "What is this video about?"
retrieve_docs = retriver.invoke(question)

context = " ".join([i.page_content for i in retrieve_docs])

final_prompt = prompt.invoke({"context":context,"question":question})

result = llm.invoke(final_prompt)
print(result.content)
