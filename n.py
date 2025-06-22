from langchain_community.document_loaders import PyMuPDFLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain.text_splitter import RecursiveCharacterTextSplitter

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

loader = PyMuPDFLoader("docs\PA - Consolidated lecture notes.pdf")
docs = loader.load()

splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
chunks = splitter.split_documents(docs)

prompt = PromptTemplate(
    template="Summarize the following text: {text}",
    input_variables=["text"]
)

chain = prompt | llm

chunks_summaries = []
for chunk in chunks:
    summary = chain.invoke({"text" :chunk.page_content})
    chunks_summaries.append(summary)

combined_summary_text = "\n".join(chunks_summaries)
final_summary = chain.invoke({"text": combined_summary_text})

# 6. Output the final summary
print(final_summary.content)
