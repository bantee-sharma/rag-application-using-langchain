from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st
import tempfile
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.prompts import PromptTemplate


load_dotenv()
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

file = st.file_uploader("Upload Your File",type=["pdf"])

if file is not None:
    with tempfile.NamedTemporaryFile(delete=False,suffix=".pdf") as tmp_file:
        tmp_file.write(file.read())
        file_path = tmp_file.name

    loader = PyPDFLoader(file_path)
    docs = loader.load()
    text = "\n".join([i.page_content for i in docs])

    prompt1 = PromptTemplate(
        template="Summarize the following text:\n {text}",
            input_variables=["text"]
        )

    prompt2 = PromptTemplate(
            template="Answer the question:\n{question} from the following text:\n{text}",
            input_variables=["question","text"]
        )

    chain1 = prompt1 | llm
    chain2 = prompt2 | llm

    if st.button("Summarize"):
        res = chain1.invoke({"text":text})        
        st.write(res.content)


    question = st.text_input("Enter your question")
    if st.button("Submit"):
        res = chain2.invoke({"question":question ,"text":text})        
        st.write(res.content)
        

st.markdown("---")
st.markdown("created by bantee")
