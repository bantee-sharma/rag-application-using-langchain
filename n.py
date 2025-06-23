from langchain_community.document_loaders import PyPDFLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import streamlit as st
import tempfile

st.title("Pdf Summarizer")
st.header("Save your time by converting long pdfs into summries")

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

try:
    file = st.file_uploader("Please upload your pdf", type=["pdf"])
except Exception as e:
    st.write("Please upload a pdf file")

if file is not None:
    with tempfile.NamedTemporaryFile(delete=False,suffix=".pdf") as tmp_file:
        tmp_file.write(file.read())
        tmp_file_path = tmp_file.name

    loader = PyPDFLoader(tmp_file_path)
    doc = loader.load()

    text = "\n".join([i.page_content for i in doc])

    prompt = PromptTemplate(
        template="You are Ai summarizer. Summarize the following text: \n {text}",
        input_variables=["text"]
    )

    chain = prompt | llm 
    response = chain.invoke(text)
