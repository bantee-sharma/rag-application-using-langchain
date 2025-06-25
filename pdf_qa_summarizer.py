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

    prompt1 = PromptTemplate(
        template="You are Ai summarizer. Summarize the following text: \n {text}",
        input_variables=["text"]
    )

    prompt2 = PromptTemplate(
            template="Answer the following question:\n{question} from the following text:\n{text}",
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
st.markdown("**Created by [Bantee Sharma](https://www.linkedin.com/in/bantee-sharma/)**")
