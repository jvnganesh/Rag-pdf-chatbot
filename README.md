# 📄 RAG-Based PDF Chatbot

A powerful **Retrieval-Augmented Generation (RAG)** chatbot that allows users to upload PDF documents and engage in a dialogue grounded strictly in the document's content. 

This project leverages **OpenAI Embeddings**, **FAISS** for high-speed vector search, and **Streamlit** for a seamless user interface. It includes professional-grade features like inline citations and a developer debug panel.

---

## 🚀 Key Features

* **Smart Document Ingestion:** Upload and process multi-page PDF documents.
* **Semantic Search:** Uses `text-embedding-3-small` for high-accuracy context retrieval.
* **Conversation-Aware:** Remembers previous turns in the chat to handle follow-up questions.
* **Fact Verification:** Inline citations point you exactly to the source text.
* **Developer Debug Panel:** Inspect similarity scores, retrieved chunks, and the raw context sent to the LLM.
* **Speed:** Local vector search powered by FAISS for near-instant response times.

---

## 🧠 How It Works

The system follows a standard RAG pipeline to ensure accuracy and reduce hallucinations:

1.  **Extraction:** Text is parsed from uploaded PDFs using `PyPDF`.
2.  **Chunking:** Content is split into manageable segments for precise retrieval.
3.  **Embedding:** Text chunks are converted into high-dimensional vectors.
4.  **Storage:** Vectors are indexed in a local **FAISS** store.
5.  **Retrieval:** When a user asks a question, the system finds the most relevant chunks.
6.  **Generation:** The LLM generates a response using *only* the retrieved context.



---

## 🛠 Tech Stack

| Component | Technology |
| :--- | :--- |
| **Language** | Python 3.9+ |
| **LLM API** | OpenAI (GPT-4o/GPT-3.5-Turbo) |
| **Embeddings** | OpenAI `text-embedding-3-small` |
| **Vector Store** | FAISS |
| **UI Framework** | Streamlit |
| **PDF Parsing** | PyPDF |

---

## 📁 Project Structure

```text
rag-pdf-chatbot/
│── app.py              # Main Streamlit application
│── requirements.txt    # Project dependencies
│── README.md           # Documentation
│── .gitignore          # Git exclusion rules
└── data/
    └── pdfs/           # Local storage for uploaded files
```

▶️ Getting Started
1. Clone the Repository
Bash
```text
git clone [https://github.com/jvnganesh/rag-pdf-chatbot.git](https://github.com/jvnganesh/rag-pdf-chatbot.git)
cd rag-pdf-chatbot
```
3. Install Dependencies
```text
pip install -r requirements.txt
```
4. Configure Environment Variables
Set your OpenAI API Key in your terminal environment:

macOS / Linux:

Bash
```text
export OPENAI_API_KEY="your_api_key_here"
Windows (PowerShell):
```
PowerShell
```text
$env:OPENAI_API_KEY="your_api_key_here"
```
4. Run the App
Bash
```text
streamlit run app.py
```
🧪 Debugging & Optimization
The built-in Debug Panel allows you to peek under the hood:

Similarity Distances: See how closely the retrieved text matches the query.

Context Inspection: View exactly what information was passed to the LLM.

Refinement: Use these insights to adjust chunk sizes or retrieval top-k settings.

⚠️ Limitations & Future Roadmap
Current Limit: Does not support scanned/image-based PDFs (requires OCR).

Roadmap: * [ ] Add Reranking (e.g., Cohere) for better precision.

[ ] Integration with Persistent Vector DBs (Pinecone/Chroma).

[ ] Support for OCR via Tesseract or Azure Form Recognizer.

[ ] Evaluation framework using RAGAS.

👤 Author
JVN Ganesh

GitHub: @jvnganesh
