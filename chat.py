import faiss
import numpy as np
from openai import OpenAI

client = OpenAI()

# Load FAISS + chunks
index = faiss.read_index("faiss.index")
chunks = np.load("chunks.npy", allow_pickle=True)

def retrieve_context(query, k=3):
    embedding = client.embeddings.create(
        model="text-embedding-3-small",
        input=query
    ).data[0].embedding

    embedding = np.array([embedding]).astype("float32")
    distances, indices = index.search(embedding, k)

    return "\n\n".join(chunks[i] for i in indices[0])

print("🤖 RAG Chatbot ready (type 'exit' to quit)\n")

while True:
    query = input("You: ")
    if query.lower() == "exit":
        break

    context = retrieve_context(query)

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=f"""
Answer the question using ONLY the context below.
If the answer is not in the context, say "I don't know".

Context:
{context}

Question:
{query}
"""
    )

    print("Bot:", response.output_text)
