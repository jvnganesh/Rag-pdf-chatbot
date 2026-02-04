import faiss
import numpy as np
from openai import OpenAI
import os

client = OpenAI()

# Load document
with open("data/knowledge.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Simple chunking
def chunk_text(text, chunk_size=500, overlap=50):
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start = end - overlap
    return chunks

chunks = chunk_text(text)

print(f"📄 Total chunks: {len(chunks)}")

# Create embeddings
embeddings = []
for chunk in chunks:
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=chunk
    )
    embeddings.append(response.data[0].embedding)

embeddings = np.array(embeddings).astype("float32")

# Create FAISS index
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(embeddings)

# Save index + chunks
faiss.write_index(index, "faiss.index")
np.save("chunks.npy", np.array(chunks))

print("✅ Ingestion complete. FAISS index saved.")
