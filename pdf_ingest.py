from pypdf import PdfReader
from openai import OpenAI
import faiss
import numpy as np
import os

client = OpenAI()

PDF_DIR = "data/pdfs"

def extract_text_from_pdf(path):
    reader = PdfReader(path)
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

all_chunks = []

for file in os.listdir(PDF_DIR):
    if file.endswith(".pdf"):
        text = extract_text_from_pdf(os.path.join(PDF_DIR, file))
        all_chunks.extend(chunk_text(text))

print(f"📄 Total PDF chunks: {len(all_chunks)}")

# Create embeddings
embeddings = []
for chunk in all_chunks:
    emb = client.embeddings.create(
        model="text-embedding-3-small",
        input=chunk
    ).data[0].embedding
    embeddings.append(emb)

embeddings = np.array(embeddings).astype("float32")

# Save to FAISS
index = faiss.IndexFlatL2(len(embeddings[0]))
index.add(embeddings)

faiss.write_index(index, "faiss.index")
np.save("chunks.npy", np.array(all_chunks))

print("✅ PDF ingestion complete")
