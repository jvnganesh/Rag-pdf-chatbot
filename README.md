# 📄 RAG-based PDF Chatbot

A Retrieval-Augmented Generation (RAG) chatbot that allows users to upload PDFs and ask questions grounded in document content.

Built using OpenAI embeddings, FAISS vector search, and a Streamlit UI with explainable citations and conversation-aware retrieval.

---

## 🚀 Features

- 📄 Upload and ingest PDF documents
- 🔍 Semantic search using embeddings + FAISS
- 💬 Chat-style interface (Streamlit)
- 📌 Inline citations for grounded answers
- 🧪 Debug panel to inspect retrieved chunks
- 🧠 Conversation-aware retrieval (memory)

---

## 🧠 How It Works (RAG Pipeline)

PDF → Text Extraction → Chunking → Embeddings → FAISS
↓
User Query → Embedding → Retrieval → LLM Answer


---

## 🛠 Tech Stack

- Python
- OpenAI API
- FAISS
- Streamlit
- PyPDF

---

## ▶️ How to Run Locally

### 1️⃣ Clone the repo
```bash
git clone https://github.com/your-username/rag-pdf-chatbot.git
cd rag-pdf-chatbot

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Set OpenAI API Key
export OPENAI_API_KEY="your_key_here"
# or on Windows:
setx OPENAI_API_KEY "your_key_here"

4️⃣ Run the app
streamlit run app.py

📄 Usage

Upload one or more PDFs

Click Process PDFs

Ask questions related to the documents

View answers with citations

⚠️ Notes

Scanned PDFs are not supported (OCR not included yet)

Vector index is rebuilt on every ingestion

API key must be set as an environment variable

📌 Future Improvements

Reranking for better retrieval

Evaluation metrics

OCR for scanned PDFs

Production deployment (FastAPI)