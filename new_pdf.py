from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.document_loaders import PyMuPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

path = "docs\PA - Consolidated lecture notes.pdf"
loader = PyMuPDFLoader(path)
document = loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=100)
chunks = text_splitter.split_documents(document)

load_dotenv()
llm = ChatGoogleGenerativeAI(model="google-2.0-flash")

prompt = PromptTemplate(
    template="Summarize the following text: {text}",
    input_variables=["text"]
)

summaries = []
for chunk in chunks:
    chunk_prompt = prompt.invoke({"text":chunk.page_content})
    response = llm.invoke(chunk_prompt)
    summaries.append(response.content)

text = "\n".join(summaries)
final_prompt = prompt.invoke({"text":text})
result = llm.invoke(final_prompt)

print(result.content)