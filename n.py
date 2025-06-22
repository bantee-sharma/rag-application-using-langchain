from langchain_community.document_loaders import PyPDFLoader






loader = PyPDFLoader("docs\PA - Consolidated lecture notes.pdf")
doc = loader.load()
print(doc)