from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_community.document_loaders import PyPDFLoader
import streamlit as st
import tempfile

load_dotenv()
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

st.title("📄 Smart PDF Summarizer & Q&A Assistant")
st.header("Upload a PDF to Summarize or Ask Questions Instantly with Google Gemini")

file = st.file_uploader("Upload your file",type=["pdf"])

if file is not None:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(file.read())
        file_name = tmp_file.name

        loader = PyPDFLoader(file_name)
        docs = loader.load()
        text = "\n".join([i.page_content for i in docs])

        prompt1 = PromptTemplate(
            template="Summarize the following text:\n{text}",
            input_variables=["text"])
        
        prompt2 = PromptTemplate(
            template="Answer the following question:{question} form the following text:{text}",
            input_variables=["question","text"]
        )

        chain1 = prompt1|llm
        chain2 = prompt2|llm

        if st.button("Summarize"):
            res = chain1.invoke({"text":text})
            st.write(res.content)
        
        question = st.text_input("Ask Your Question")
        if st.button("Answer"):
            res = chain2.invoke({"question":question,"text":text})
            st.write(res.content)

st.markdown("___")
st.markdown("***Created by Bantee Sharma***")