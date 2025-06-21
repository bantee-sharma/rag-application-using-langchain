from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.document_loaders import PyMuPDFLoader


path = "docs\PA - Consolidated lecture notes.pdf"
loader = PyMuPDFLoader(path)

document = loader.load()
print(document)
