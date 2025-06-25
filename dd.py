from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st
import tempfile
from langchain_community.document_loaders import PyPDFLoader


load_dotenv()
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

file = st.file_uploader("Upload Your File",type=["pdf"])

if file is not None:
    with tempfile.NamedTemporaryFile(delete=False,suffix=".pdf") as tmp_file:
        tmp_file.write(file.read())
        file_path = tmp_file.name

        loader = PyPDFLoader(file_path)
        docs = loader.load()
        