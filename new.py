from langchain_community.document_loaders import TextLoader,PyMuPDFLoader, UnstructuredWordDocumentLoader
from pathlib import Path
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

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
        all_documents.extend(document)
    return all_documents

docs = my_docs("docs")


text_split = RecursiveCharacterTextSplitter(chunk_size = 1000, chunk_overlap = 100)
chunks = text_split.split_documents(docs)

embedd = HuggingFaceEmbeddings()
db = FAISS.from_documents(chunks,embedd)

retriever = db.as_retriever(search_type="similarity", kwargs={'k':3})

prompt = PromptTemplate(
    template='''Yor are a helpfull AI assistant. Answer the question from the following context.
    If the answer is not present in the context, respond with: "The answer is not available in the provided context.
            
    Context:{context}
    Question:{question}
    Answer: ''',
    input_variables=["context","question"])
    
query = "What is loss function"
retriev_docs = retriever.invoke(query)

context = "".join([i.page_content for i in retriev_docs])

final_prompt = prompt.invoke({"context":context,"question":query})

response = llm.invoke(final_prompt)
print(response)

