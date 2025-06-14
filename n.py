from langchain_community.document_loaders import PyMuPDFLoader,TextLoader, UnstructuredWordDocumentLoader
from pathlib import Path
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.tools import tool
from langchain.agents import create_react_agent, AgentExecutor
from langchain import hub
import requests

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

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

@tool
def doc_qa_tool(question:str)->str:
    "Yor are a helpfull AI assistant. Answer the question from the following context."
    retriev_docs = retriever.invoke(question)
    context = "".join([i.page_content for i in retriev_docs])
    qa_prompt = PromptTemplate(
    template='''Yor are a helpfull AI assistant. Answer the question from the following context.
    If the answer is not present in the context, respond with: "The answer is not available in the provided context.
            
    Context:{context}
    Question:{question}
    Answer: ''',
    input_variables=["context","question"])
    final_prompt = qa_prompt.invoke({"context":context,"question":question})
    response = llm.invoke(final_prompt)
    return response.content

@tool
def weather(city:str)-> str:
    "Fetch the Current weather of the city"
    url = "https://api.weatherstack.com/current?access_key=2eab0e8b57aa4c3082a9f22e95baa467"
    city_srting = {"query":city}
    temp = requests.get(url=url,params=city_srting)
    return temp.json()

prompt = hub.pull("hwchase17/react")

agent = create_react_agent(
    llm=llm,
    prompt=prompt,
    tools=[doc_qa_tool,weather]
)

age_exe = AgentExecutor(
    agent=agent,
    tools=[doc_qa_tool,weather],
    verbose=True
)
print("Hii, I am you personal assistant ask me anything!. For quiting conversation type exit or quit")
while True:
    question = input("Ask me: ").strip()
    if question.lower() in ["quit","exit"]:
        print("Exiting...Bye....")
        break
    else:
        response =age_exe.invoke({"input" :question})
        print("AI: ",response)