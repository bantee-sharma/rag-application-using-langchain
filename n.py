from langchain_community.document_loaders import PyMuPDFLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

loader = PyMuPDFLoader("docs\PA - Consolidated lecture notes.pdf")
doc = loader.load()

text = "\n".join([i.page_content for i in doc])

prompt = PromptTemplate(
    template="You are Ai summarizer. Summarize the following text: \n {text}",
    input_variables=["text"]
)

chain = prompt | llm 
response = chain.invoke(text)
print(response.content)