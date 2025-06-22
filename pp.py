from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

prompt = PromptTemplate(
    template="Answer the following question:{question}",
    input_variables=["question"]
)

query = {"question": "What is AI?"}

chain = prompt|llm

res = chain.invoke(query)
print(res)