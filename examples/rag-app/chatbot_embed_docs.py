from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

documents = [
    "Foxnuts are rich in protein and antioxidants.",
    "Machine learning is a subset of artificial intelligence.",
    "Vector databases are used for semantic search.",
]

def create_embeddings():
    embeddings = [model.encode(doc) for doc in documents]
    return embeddings
