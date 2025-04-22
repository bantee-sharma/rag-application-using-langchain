from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_core.prompts import PromptTemplate
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings

video_id = 'Gfr50f6ZBvo'

try:
    transcript_list = YouTubeTranscriptApi.get_transcript(video_id=video_id,languages=["en"])

    transcript = " ".join(i["text"] for i in transcript_list)
except TranscriptsDisabled:
    print("No caption availble for this video")

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000, chunk_overlap=200
)

chunk = text_splitter.create_documents([transcript])


embeddings =HuggingFaceEmbeddings()

db = FAISS.from_documents(chunk,embedding=embeddings)

retriever = db.as_retriever(search_type="similarity", search_kwargs={"k":4})

res = retriever.invoke("what is deepmind")

print(res)