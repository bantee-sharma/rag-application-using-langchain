from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.document_loaders import PyMuPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

path = "docs\PA - Consolidated lecture notes.pdf"
loader = PyMuPDFLoader(path)
document = loader.load()

text = "".join([i.page_content for i in document])
print(len(text))



load_dotenv()
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

prompt = PromptTemplate(
    template="Summarize the following text: {text}",
    input_variables=["text"]
)

chain = prompt | llm

res = chain.invoke({"text": text})
#print(res)