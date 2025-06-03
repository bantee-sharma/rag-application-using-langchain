from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from youtube_transcript_api import  YouTubeTranscriptApi, TranscriptsDisabled,NoTranscriptFound
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

load_dotenv()

video_id = "E3oG313_kps"

try:
    transcript_text = YouTubeTranscriptApi.get_transcript(video_id=video_id,languages=["hi"])
    text = " ".join([i["text"] for i in transcript_text])
    

except NoTranscriptFound:
    print("No Captions found for this video.")

text_spiltter = RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=100)
chunks = text_spiltter.create_documents([text])

embedd = HuggingFaceEmbeddings()
vector_store = FAISS.from_documents(chunks,embedd)

retriever = vector_store.as_retriever(search_type = "similarity",kwargs={"k":5})

query = "What is this about?"
print(retriever.invoke(query))