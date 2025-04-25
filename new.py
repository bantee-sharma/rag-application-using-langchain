from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()



video_id = "QbFA_4fDQ9k"

#video_id = "Gfr50f6ZBvo&t=1s"
try:
    transcript = YouTubeTranscriptApi.get_transcript(video_id=video_id, languages=["hi"])
    text = " ".join([i["text"] for i in transcript])
except:
    print("No captions available for this videos.")

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size = 500, chunk_overlap=50
)

chunk = text_splitter.create_documents([text])
embeddings = HuggingFaceEmbeddings()

vector_store = FAISS.from_documents(chunk,embeddings)

retrieve = vector_store.as_retriever(search_type='similarity', kwargs={"k":2})

prompt = PromptTemplate(
    template="""You are a helpfull ai asistant. 
    Give answer only from this transcript.
    if context is insufficient, just say you don't know
    {context}
    Question: {question}""",
    input_variables= ["context","question"]
    )

question = "Summarize this video in english."

retrieve_doc = retrieve.invoke(question)


context = " ".join([i.page_content for i in retrieve_doc])

llm = ChatGoogleGenerativeAI(model = "gemini-2.0-flash")

final_prompt = prompt.invoke({"context": context, "question": question})

res = llm.invoke(final_prompt)
print(res.content)
