from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.prompts import PromptTemplate
import streamlit as st
import tempfile


st.title("AI summarizer")
st.header("Convert your long text into small summaries")


load_dotenv()
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

file_upload = st.file_uploader("Upload your file",type=[".pdf"])

if file_upload is not None:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(file_upload.read())
        file_name = tmp_file.name

    loader = PyPDFLoader(file_name)
    doc = loader.load()

    text = "\n".join([i.page_content for i in doc])

prompt1 = PromptTemplate(
    template="You are an helpfull AI assistant. Summarize the following text:\n {text}",
    input_variables=["text"]
)

prompt2 = PromptTemplate(
    template="You are an helpfull AI assistant. Answer the question: {question} from following text :\n {text}",
    input_variables=["question","text"]
)

chain1 = prompt1 | llm
chain2 = prompt2 | llm

if st.button("Summarize"):

    res = chain1.invoke({"text":text})
    st.write(res.content)


question = st.text_input("Ask any question:")
if st.button("Summarize"):

    res = chain2.invoke({"question":question ,"text":text})
    st.write(res.content)