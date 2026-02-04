# 📄 RAG-Based PDF Chatbot

A **Retrieval-Augmented Generation (RAG)** chatbot that allows users to upload PDF documents and ask questions grounded strictly in the document content.

Built using **OpenAI embeddings**, **FAISS vector search**, and a **Streamlit** interface with **citations, debugging tools, and conversation-aware retrieval**.

---

## 🚀 Features

- 📄 Upload and ingest PDF documents  
- 🔍 Semantic search using vector embeddings  
- 💬 Chat-style UI built with Streamlit  
- 📌 Inline citations for every factual answer  
- 🧪 Debug panel to inspect retrieved chunks and similarity scores  
- 🧠 Conversation-aware retrieval (chat memory)  
- ⚡ Fast local vector search using FAISS  

---

## 🧠 How It Works (RAG Pipeline)

PDF → Text Extraction → Chunking → Embeddings → FAISS Vector Store
↓
User Query → Embedding → Similarity Search → Context → LLM Answer


### Why RAG?
- Prevents hallucinations  
- Keeps answers grounded in source documents  
- Allows dynamic, up-to-date knowledge without fine-tuning  

---

## 🛠 Tech Stack

- **Language:** Python  
- **LLM API:** OpenAI  
- **Embeddings:** `text-embedding-3-small`  
- **Vector Store:** FAISS  
- **UI:** Streamlit  
- **PDF Parsing:** PyPDF  

---

## 📁 Project Structure

rag-pdf-chatbot/
│── app.py # Streamlit application
│── requirements.txt # Dependencies
│── README.md
│── .gitignore
│── data/
│ └── pdfs/ # (Optional) PDF storage


> ⚠️ Vector index files (`faiss.index`, `chunks.npy`) are generated at runtime and are not committed.

---

## ▶️ Running the Project Locally

### 1️⃣ Clone the repository
```bash
git clone https://github.com/jvnganesh/rag-pdf-chatbot.git
cd rag-pdf-chatbot
2️⃣ Install dependencies
pip install -r requirements.txt
3️⃣ Set OpenAI API Key
Linux / macOS

export OPENAI_API_KEY="your_api_key_here"
Windows (PowerShell)

setx OPENAI_API_KEY "your_api_key_here"
Restart the terminal after setting the key.

4️⃣ Run the application
streamlit run app.py
📄 Usage Instructions
Upload one or more text-based PDFs

Click “Process PDFs” to ingest documents

Ask questions related to the uploaded content

View answers with inline citations

Enable Debug Panel to inspect retrieved chunks

🧪 Debug Panel
The debug panel shows:

Retrieved document chunks

Similarity distances

Context used by the LLM

This helps with:

Understanding retrieval behavior

Debugging hallucinations

Improving chunking and retrieval strategies

⚠️ Limitations
Scanned PDFs are not supported (OCR not included)

Vector index is rebuilt on each ingestion

Designed for local / demo usage (not production-scale yet)

📌 Future Improvements
Reranking for higher retrieval accuracy

Evaluation metrics for RAG performance

OCR support for scanned PDFs

Production deployment using FastAPI

Persistent vector storage

📜 License
MIT License

👤 Author
JVN Ganesh
GitHub: https://github.com/jvnganesh
