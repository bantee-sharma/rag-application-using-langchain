from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_core.prompts import PromptTemplate
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.chains import retrieval_qa


video_id = 'Gfr50f6ZBvo'

try:
    transcript_text = YouTubeTranscriptApi.get_transcript(video_id=video_id,languages=["en"])
    text = " ".join([i["text"] for i in transcript_text])
except TranscriptsDisabled:
    print("No caption avilable for this video")

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,chunk_overlap=200
)

chunk = text_splitter.create_documents([text])

embeddings = HuggingFaceEmbeddings()

vector_store = FAISS.from_documents(chunk,embedding=embeddings)

retriever = vector_store.as_retriever(search_type="similarity", kwargs={"k":1})

res = retriever.invoke("What id deepmind?")

prompt = PromptTemplate(
    template='''You are a helpfull assistant. Answer only from provided transcript context. if context is insufficient, just say you do not know.

    {context}
    Question = {question}''',
    input_variables=["context","question"]
)

question = "Is there any topic disscused about aliens in this video"

ret_docs = retriever.invoke(question)
print(ret_docs)