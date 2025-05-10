from youtube_transcript_api import YouTubeTranscriptApi,TranscriptsDisabled
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import re
import streamlit as st

load_dotenv()

# STEP 1: Accept full URL or ID
input_link = 'https://www.youtube.com/watch?v=oHry5RRI4KU'  # or just 'oHry5RRI4KU'

# STEP 2: Extract video ID from URL
def extract_video_id(link_or_id):
    pattern = r"(?:v=|\/)([0-9A-Za-z_-]{11}).*"
    match = re.search(pattern, link_or_id)
    return match.group(1) if match else link_or_id


video_id = extract_video_id(input_link)

try:
    transcript_text = YouTubeTranscriptApi.get_transcript(video_id=video_id,languages=["en",'hi'])
    text = " ".join([i["text"] for i in transcript_text])
except TranscriptsDisabled:
    print("No captions available for this video.")

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500, chunk_overlap=100
)

chunk = text_splitter.create_documents([text])

embedd = HuggingFaceEmbeddings()
vector_store = FAISS.from_documents(chunk,embedd)

retriever = vector_store.as_retriever(search_type="similarity", kwargs=[{"k":2}])

prompt = PromptTemplate(
    template= '''You are a helpful AI assistant.
    Answer the question from the following context.
    If the context is insufficient, just say, I don't Know.
    if quenstion in englsih than answer in english.
    {context}
    Question: {question}''',
    input_variables=['context','question']
)

question = "Is there any topic disscused about war in this video, if yes then what was discussed"
retriever_docs = retriever.invoke(question)

context = " ".join([i.page_content for i in retriever_docs])

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

final_prompt = prompt.invoke({"context":context, "question": question})

answer = llm.invoke(final_prompt)
print(answer.content)


