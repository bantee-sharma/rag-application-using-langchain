from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_community.document_loaders import PyMuPDFLoader,UnstructuredPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-2.5-pro-preview-06-05")

path = "docs\dl-curriculum.pdf"
loader = PyMuPDFLoader(path)
docs = loader.load()

doc = " ".join([i.page_content for i in docs])

splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
chunks = splitter.split_documents(docs)

prompt = PromptTemplate(
    template="Summarize the followign context: {text}",
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