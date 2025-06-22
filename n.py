from langchain_community.document_loaders import PyMuPDFLoader






loader = PyMuPDFLoader("docs\PA - Consolidated lecture notes.pdf")
doc = loader.load()
print(doc)