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

splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
chunks = splitter.split_documents(docs)

text = "".join([i.page_content for i in chunks])


prompt = PromptTemplate(
    template="Summarize the following text: {text}",
    input_variables=["text"]
)

final = prompt.invoke({"text": text})
res = llm.invoke(final)

print(res.content)
