from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_community.document_loaders import PyMuPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

path = "docs\dl-curriculum.pdf"
loader = PyMuPDFLoader(path)
docs = loader.load()

prompt = PromptTemplate(
    template="Summarize the following text: {text}",
    input_variables=["text"]
)

final = prompt.invoke(docs)
res = llm.invoke(final)

print(res)
