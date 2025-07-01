from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.prompts import PromptTemplate
import streamlit as st


st.title("AI summarizer")
st.header("Convert your long text into small summaries")


load_dotenv()
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

file_upload = st.file_uploader("Upload your file",type=[".pdf"])

if file_upload is not None:

    loader = PyPDFLoader("docs/dl-curriculum.pdf")
    doc = loader.load()

    text = "\n".join([i.page_content for i in doc])

prompt1 = PromptTemplate(
    template="You are an helpfull AI assistant. Summarize the following text:\n {text}",
    input_variables=["text"]
)

chain = prompt1 | llm


if st.button("Summarize"):

    res = chain.invoke({"text":text})
    st.write(res.content)