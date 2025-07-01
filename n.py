from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader



load_dotenv()
llm = ChatGoogleGenerativeAI()

loader = PyPDFLoader("docs/dl-curriculum.pdf")
doc = loader.load()
print(doc)