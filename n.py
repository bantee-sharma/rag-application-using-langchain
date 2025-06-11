from langchain_community.document_loaders import PyMuPDFLoader,TextLoader, UnstructuredWordDocumentLoader
from pathlib import Path


def my_docs(folder_path):
    all_docs = []
    for file in Path(folder_path).glob("*"):
        if file.suffix == ".pdf":
            loader = PyMuPDFLoader(str(file))
        elif file.suffix == ".txt":
            loader = TextLoader(str(file),encoding="utf-8")
        elif file.suffix == ".docx":
            loader = UnstructuredWordDocumentLoader(str(file))
        else:
            print(f"Skipping unsupported file type: {file.name}")
            continue
        
        document = loader.lazy_load()
        all_docs.extend(document)
    return all_docs

doc = my_docs("docs")
print(doc)

