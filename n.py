from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader



load_dotenv()
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

loader = PyPDFLoader("docs/dl-curriculum.pdf")
doc = loader.load()

text = " \n ".join([i.page_content for i in doc])
print(text)