
## 🎥 YouTube Transcript QA Bot — Ask Questions About Any Video! 🤖💬


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

FAISS (Vector Store)

Hugging Face Transformers (Embeddings)

Google Generative AI (Gemini)

YouTube Transcript API


