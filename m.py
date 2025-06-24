from langchain_community.document_loaders import PyPDFLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import streamlit as st
import tempfile

st.title("AI-Powered PDF Summarizer")
st.header("Instantly Summarize Lengthy PDFs with the Power of Generative AI")

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

file_name = st.file_uploader("Upload your pdf", type=["pdf"])
