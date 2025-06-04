from langchain_community.document_loaders import TextLoader,PyMuPDFLoader, UnstructuredWordDocumentLoader
from pathlib import Path
from langchain.text_splitter import RecursiveCharacterTextSplitter



def my_docs(folder_path):
    all_documents = []

    for file in Path(folder_path).glob("*"):
        if file.suffix == ".pdf":
            loader = PyMuPDFLoader(str(file))
        elif file.suffix == ".txt":
            loader = TextLoader(str(file),encoding="utf-8")
        elif file.suffix == ".docx":
            loader = UnstructuredWordDocumentLoader(str(file))
        else:
            continue

        document = loader.load()
        all_documents.append(document)
    return all_documents

docs = my_docs("docs")


text_split = RecursiveCharacterTextSplitter(chunk_size = 1000, chunk_overlap = 100)
chunks = text_split.split_documents(docs)
print(chunks)