from langchain_community.document_loaders import PyMuPDFLoader,TextLoader, UnstructuredWordDocumentLoader
from pathlib import Path
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate

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

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
chunks = text_splitter.split_documents(doc)

embedd = HuggingFaceEmbeddings()
db = FAISS.from_documents(chunks,embedd)

retriever = db.as_retriever(search_type="similarity",kwargs={"k":5})

prompt = PromptTemplate(
    template='''You are a helpfull Assistant.
    Answer the question from the following context : {context}.
    If the answer is not present in the context, respond with: "The answer is not available in the provided context.Question: {question}''',
    input_variables=["context","question"]
)

query = "What is sql?"
context = retriever.invoke(query)
print(context)