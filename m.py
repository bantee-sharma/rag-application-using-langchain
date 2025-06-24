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


if file_name is not None:
    with tempfile.NamedTemporaryFile(suffix=".pdf",delete=False) as tmp_file:
        tmp_file.write(file_name.read())
        file_path = tmp_file.name

        loader = PyPDFLoader(file_path)
        docs = loader.load()

        text = "\n".join([i.page_content for i in docs])

        prompt1 = PromptTemplate(
            template="Summarize the following text:{text}",
            input_variables=["text"]
        )

        chain = prompt1|llm

        if st.button("Summarize"):
            response = chain.invoke(text)
            st.write(response.content)


