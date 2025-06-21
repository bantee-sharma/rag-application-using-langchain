from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.document_loaders import PyPDFLoader

path = "docs\PA - Consolidated lecture notes.pdf"
loader = PyPDFLoader(path)

document = loader.load()
print(document)
