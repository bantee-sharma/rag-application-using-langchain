from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.document_loaders import PyMuPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

path = "docs\PA - Consolidated lecture notes.pdf"
loader = PyMuPDFLoader(path)
document = loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=100)
chunks = text_splitter.split_documents(document)
print(len(chunks))


