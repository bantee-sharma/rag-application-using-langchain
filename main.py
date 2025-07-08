from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled, NoTranscriptFound, VideoUnavailable
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

video_id = 'MdeQMVBuGgY'

try:
    transcript_text = YouTubeTranscriptApi.get_transcript(video_id, languages=['hi',"en"])
    text = "".join([i["text"] for i in transcript_text])
except TranscriptsDisabled:
    print("❌ Transcripts are disabled for this video.")
except NoTranscriptFound:
    print("❌ No transcript found for the specified language.")
except VideoUnavailable:
    print("❌ Video is unavailable.")
except Exception as e:
    print(f"❌ An unexpected error occurred: {e}")

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=100)
docs = text_splitter.create_documents([text])

embedd = HuggingFaceEmbeddings()
vector_store = FAISS.from_documents(docs,embedd)
retriever = vector_store.as_retriever(search_type="similarity",kwargs=[{"k":5}])



prompt = PromptTemplate(
    template="You are a helffull Ai Assistant. Answer the following Question:{question} from the following context:{context}",
    input_variables=["question","context"]
)


print("Yor CLI is ready")

while True:
    query = input()
    if query.lower().strip() in ["exit","quit"]:
        print("Bye...")
        break
    retriever_docs = retriever.invoke(query)
    context = " ".join([i.page_content for i in retriever_docs])


    final_prompt = prompt.invoke({"question":query,"context":context})

    
    
    response = llm.invoke(final_prompt)
    print("Answer",response.content)