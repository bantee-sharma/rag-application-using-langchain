from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from youtube_transcript_api import  YouTubeTranscriptApi, TranscriptsDisabled,NoTranscriptFound
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

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

prompt = PromptTemplate(
    prompt = PromptTemplate(
    template='''
You are an intelligent assistant designed to answer questions based on the transcript of a YouTube video.

Use only the information provided in the transcript context below to answer the user's question. Be concise, accurate, and informative.

If the information needed to answer the question is not present in the context, respond with:
"Sorry, I couldn't find the answer to that question in the video transcript."

Transcript Context:
{context}

User Question:
{question}

Answer:''',
    input_variables=["context", "question"]
)

)

print("Knowledge Assistant ready! Type 'exit' to quit.")

while True:
    query = input("Ask Anything: ").strip()
    if query.lower() in ["exit","quit"]:
        print("Exiting....")
        break
    else:
        retrieve_docs = retriever.invoke(query)
        context = "".join([i.page_content for i in retrieve_docs])

        final_prompt = prompt.invoke({"context":context,"question":query})

        response = llm.invoke(final_prompt)
        print("AI: ",response.content)
