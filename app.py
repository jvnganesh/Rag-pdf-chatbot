import streamlit as st
from pypdf import PdfReader
import faiss
import numpy as np
from openai import OpenAI

# ---------- Config ----------
st.set_page_config(
    page_title="RAG Chatbot",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 RAG Chatbot")
st.caption("Powered by OpenAI + FAISS")

client = OpenAI()

# ---------- Sidebar ----------
st.sidebar.title("🧪 Debug Panel")
debug = st.sidebar.checkbox("Show retrieved chunks")

st.sidebar.subheader("📄 Upload PDFs")
uploaded_files = st.sidebar.file_uploader(
    "Upload PDF files",
    type=["pdf"],
    accept_multiple_files=True
)
process_btn = st.sidebar.button("📥 Process PDFs")

# ---------- PDF Utilities ----------
def extract_text_from_pdf(file):
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text


def chunk_text(text, chunk_size=500, overlap=50):
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start = end - overlap
    return chunks

# ---------- Load Vector Store ----------
@st.cache_resource
def load_vectorstore():
    index = faiss.read_index("faiss.index")
    chunks = np.load("chunks.npy", allow_pickle=True)
    return index, chunks

# ---------- Ingest PDFs ----------
if process_btn and uploaded_files:
    all_chunks = []

    with st.spinner("Processing PDFs..."):
        for pdf in uploaded_files:
            text = extract_text_from_pdf(pdf)
            chunks_pdf = chunk_text(text)
            all_chunks.extend(chunks_pdf)

        embeddings = []
        for chunk in all_chunks:
            emb = client.embeddings.create(
                model="text-embedding-3-small",
                input=chunk
            ).data[0].embedding
            embeddings.append(emb)

        embeddings = np.array(embeddings).astype("float32")

        index = faiss.IndexFlatL2(len(embeddings[0]))
        index.add(embeddings)

        faiss.write_index(index, "faiss.index")
        np.save("chunks.npy", np.array(all_chunks))

    # IMPORTANT: clear cached vectorstore
    load_vectorstore.clear()
    st.sidebar.success("✅ PDFs processed successfully!")
    st.rerun()

# ---------- Load index ----------
try:
    index, chunks = load_vectorstore()
except:
    st.warning("⚠️ No vector store found. Please upload PDFs first.")
    st.stop()

# ---------- Retrieval ----------
def retrieve_context(query, k=8):
    embedding = client.embeddings.create(
        model="text-embedding-3-small",
        input=query
    ).data[0].embedding

    embedding = np.array([embedding]).astype("float32")
    distances, indices = index.search(embedding, k)

    retrieved = []
    for rank, idx in enumerate(indices[0]):
        retrieved.append({
            "id": int(idx),
            "content": chunks[idx],
            "distance": float(distances[0][rank])
        })

    return retrieved

# ---------- Session State ----------
if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------- Display Chat History ----------
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ---------- Chat Input ----------
user_input = st.chat_input("Ask something from your PDFs...")

if user_input:
    # User message
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )
    with st.chat_message("user"):
        st.markdown(user_input)

    # Retrieve context
    retrieved_chunks = retrieve_context(user_input)

    context_text = ""
    for i, ch in enumerate(retrieved_chunks):
        context_text += f"[{i}] {ch['content']}\n\n"

    # LLM response
    response = client.responses.create(
        model="gpt-4.1-mini",
        input=f"""
You are a factual assistant.

Answer the question using ONLY the context below.
Every factual sentence MUST include a citation like [0], [1], etc.
If the answer is not present, say "I don't know".

Context:
{context_text}

Question:
{user_input}
"""
    )

    answer = response.output_text

    # Assistant message
    st.session_state.messages.append(
        {"role": "assistant", "content": answer}
    )
    with st.chat_message("assistant"):
        st.markdown(answer)

        with st.expander("📌 Sources"):
            for i, ch in enumerate(retrieved_chunks):
                st.markdown(f"[{i}] Chunk ID: {ch['id']}")

    # ---------- Debug Panel ----------
    if debug:
        st.sidebar.subheader("Retrieved Chunks")
        for i, ch in enumerate(retrieved_chunks):
            st.sidebar.markdown(f"**[{i}] Distance:** {ch['distance']:.4f}")
            st.sidebar.markdown(ch["content"])
            st.sidebar.markdown("---")
