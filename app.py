from youtube_transcript_api import YouTubeTranscriptApi,TranscriptsDisabled
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

video_id = 'E3oG313_kps'

try:
    transcript_text = YouTubeTranscriptApi.get_transcript(video_id=video_id,languages=['hi'])
    text = " ".join([i["text"] for i in transcript_text])
    

except TranscriptsDisabled:
    print("No captions available for this video.")


text_split = RecursiveCharacterTextSplitter(
    chunk_size = 1000, chunk_overlap = 100
)

chunk = text_split.create_documents([text])

embedd = HuggingFaceEmbeddings()

vector_store = FAISS.from_documents(chunk,embedd)

retriever = vector_store.as_retriever(search_type="similarity", kwargs={'k':3})

prompt = PromptTemplate(
    template= '''You are a helpful AI assistant.
    Answer the question based on the following context.
    If context is insufficient, just say, "I don't know."
    if anyone ask the quesion in english, then answer in Englsih.
    {context}
    Question :
    {question}''',
    input_variables=["context","question"]
)

question = "Summary of this video"

retriever_docs = retriever.invoke(question)

context = " ".join([i.page_content for i in retriever_docs])

final_prompt = prompt.invoke({"context":context, "question": question})

res = llm.invoke(final_prompt)

print(res.content)