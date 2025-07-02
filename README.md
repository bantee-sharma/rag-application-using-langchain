
## 1. 🎥 YouTube Transcript QA Bot — Ask Questions About Any Video! 🤖💬


This project lets you ask questions about any YouTube video using its transcript! 
It combines the power of LangChain, Google Generative AI (Gemini), and FAISS to create a smart,
context-aware assistant that can answer based on video content.


**🚀 Features**

📺 Automatically fetches English transcripts from YouTube videos

🔗 Splits the transcript into manageable chunks using LangChain

🧠 Embeds the transcript using HuggingFace Embeddings

🔍 Stores chunks in FAISS for similarity-based retrieval

💬 Uses Google Gemini (via LangChain) to answer questions contextually

❓ Custom prompt ensures the model only answers from available transcript context

**🛠️ Tech Stack**


**Python**

**LangChain**

**FAISS (Vector Store)**

**Hugging Face Transformers (Embeddings)**

**Google Generative AI (Gemini)**

**YouTube Transcript API**


## 2.📄 AI-Powered PDF Summarizer 🔍✨

Instantly Summarize & Question PDFs Using Generative AI


This project is a Streamlit web app that uses Google’s Gemini 2.0 Flash model to quickly summarize long PDF documents and answer custom user questions based on their content. Whether you're reading research papers, reports, or manuals — this tool gives you instant insights with the power of LLMs.

**✅ Features**

- 📥 Upload PDFs directly in the browser

- 📚 Automatic summarization of large documents

- ❓ Ask custom questions based on the PDF content

⚡ Powered by Gemini 2.0 Flash for blazing-fast, high-quality answers

🖥️ Clean, user-friendly interface built with Streamlit


**🧠 Tech Stack**

LangChain – Prompt management and chaining

Google Generative AI (Gemini 2.0 Flash) – For LLM-based summarization and Q&A

Streamlit – Frontend for interactive UI

PyPDFLoader – Load and parse PDF files

dotenv – Secure API key management
