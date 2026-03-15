import numpy as np
from embed_documents import create_embeddings, documents, model

vectors = create_embeddings()

def retrieve(query):
    q_vec = model.encode(query)

    scores = []
    for i, vec in enumerate(vectors):
        sim = np.dot(q_vec, vec) / (np.linalg.norm(q_vec) * np.linalg.norm(vec))
        scores.append((sim, documents[i]))

    scores.sort(reverse=True)

    return [doc for _, doc in scores[:2]]
