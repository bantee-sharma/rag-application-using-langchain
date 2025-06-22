from langchain_community.document_loaders import PyMuPDFLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

loader = PyMuPDFLoader("docs\PA - Consolidated lecture notes.pdf")
doc = loader.load()

prompt = PromptTemplate(
    template="Summarize the following text: {text}",
    input_variables=["text"]
)

chain = prompt | llm

res = chain.invoke({"text":doc})
print(res)