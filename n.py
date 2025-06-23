from langchain_community.document_loaders import PyMuPDFLoader




loader = PyMuPDFLoader("docs\PA - Consolidated lecture notes.pdf")
doc = loader.load()

text = "\n".join([i.page_content for i in doc])
print(len(text))