# EndeeAI – RAG Research Assistant

> **AI-powered knowledge chatbot** built with the **Endee Vector Database**, Sentence Transformers, FastAPI, and Streamlit. Implements a full RAG (Retrieval-Augmented Generation) pipeline for semantic document retrieval and AI answer generation.

This repository features the **Endee high-performance vector engine** along with a production-ready **RAG Research Assistant** implementation.

---

## Problem Statement

Large Language Models (LLMs) are powerful but have a key limitation — **they cannot access private documents, domain-specific knowledge, or real-time information**. Without external retrieval, LLMs hallucinate or return generic answers.

## Solution

This project implements a **Retrieval-Augmented Generation (RAG)** pipeline that:

1.  **Converts** documents into dense vector embeddings (384-dimensional)
2.  **Stores** embeddings in the **Endee Vector Database** using the official Python SDK
3.  **Retrieves** semantically relevant documents using cosine similarity search
4.  **Generates** an AI answer grounded in the retrieved context

The result: an AI that can accurately answer questions using your own knowledge base.

---

## System Architecture

```text
User Question
     ↓
Sentence Transformer (all-MiniLM-L6-v2)
     ↓    [384-dim dense vector]
Endee Vector Database  ←── upsert (ingest.py)
     ↓    [cosine similarity search, top-k]
Retrieved Documents (with meta + source)
     ↓
RAG Prompt Builder
     ↓
LLM (OpenAI / HuggingFace / Ollama)
     ↓
Answer + Sources → FastAPI + Streamlit UI
```

---

## How Endee is Used

Endee is used as the **core vector database** for this project:

| Operation | Endee SDK Call |
| :--- | :--- |
| **Create index** | `client.create_index(name, dimension=384, space_type="cosine", precision=Precision.INT8)` |
| **Upsert vectors** | `index.upsert([{id, vector, meta, filter}])` |
| **Search** | `index.query(vector=query_vec, top_k=3)` |

Endee's HNSW-based approximate nearest-neighbor search makes this significantly faster than brute-force cosine similarity — crucial for production-scale retrieval.

### Why Endee vs Other Vector DBs?

*   🚀 **High-performance**: Handles millions of vectors with millisecond latency
*   🔍 **Advanced filtering**: Filter by metadata fields (category, source, topic)
*   🔗 **Hybrid search**: Combines dense vector + sparse keyword retrieval
*   🛠️ **Simple SDK**: One-line Python client `Endee()` connects to the local server
*   🏗️ **Production-ready**: CPU-optimized (AVX2/AVX512/NEON), Docker-deployable

---

## Features

*   ✅ Vector embeddings via Sentence Transformers (384-dim)
*   ✅ Semantic document retrieval using Endee (cosine similarity)
*   ✅ Full RAG pipeline with prompt construction
*   ✅ REST API via FastAPI (`/chat`, `/search` endpoints)
*   ✅ Chat UI via Streamlit (with session history & source inspection)
*   ✅ Metadata filtering support (category, source)
*   ✅ Easily extensible with OpenAI / HuggingFace LLM

---

## Tech Stack

| Layer | Technology |
| :--- | :--- |
| **Vector Database** | Endee (open-source, localhost:8080) |
| **Embeddings** | Sentence Transformers `all-MiniLM-L6-v2` |
| **Backend API** | FastAPI + Uvicorn |
| **Chat UI** | Streamlit |
| **Language** | Python 3.10+ |

---

## Project Structure

```text
endee/
├── src/                 # Core Endee C++ Engine
├── examples/
│   └── rag-app/         # Full RAG Research Assistant
│       ├── app.py           # FastAPI backend
│       ├── ui.py            # Streamlit interface
│       ├── rag_pipeline.py  # Core RAG logic
│       ├── ingest.py        # Data ingestion script
│       └── data/            # Knowledge base
├── .github/workflows/   # CI/CD Pipelines
└── README.md            # This file
```

---

## Setup & Run

### 1. Start the Endee Server
```bash
# Clone and build the engine
git clone https://github.com/bharatnanda001/endee.git
cd endee
chmod +x ./install.sh ./run.sh
./install.sh --release --avx2
./run.sh
```
*The Endee server starts at: http://localhost:8080*

### 2. Launch the RAG App
```bash
cd examples/rag-app
pip install -r requirements.txt

# Ingest data
python ingest.py

# Start API
uvicorn app:app --reload

# Start UI (new terminal)
streamlit run ui.py
```

---

## API Reference

### `GET /chat`
Full RAG answer with retrieved documents.
`http://localhost:8000/chat?q=What+is+RAG?`

### `GET /search`
Raw semantic search results from Endee.
`http://localhost:8000/search?q=vector+database&top_k=3`

---

## License

Apache 2.0 — Built on [Endee](https://github.com/endee-io/endee)
