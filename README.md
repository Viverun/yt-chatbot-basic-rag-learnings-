# 📚 Learning RAG (My LangChain Journey)

## 🤖 Building a Basic RAG Chatbot

This repository documents my journey of learning **Retrieval-Augmented Generation (RAG)** using LangChain, local LLMs, embeddings, and vector databases.

The goal is to understand how modern AI applications combine document retrieval with language models to provide grounded answers.

## 🚀 Current Progress

### Data Ingestion

* ✅ Implemented a **YouTube Transcript Fetcher** using `youtube-transcript-api`.
* ✅ Built a **YouTube URL Parser** to automatically extract video IDs from different YouTube URL formats.
* ✅ Created a modular ingestion pipeline for loading transcript data.

### Document Processing & Indexing

* ✅ Implemented text chunking using `RecursiveCharacterTextSplitter`.
* ✅ Generated embeddings using local embedding models through Ollama.
* ✅ Built a FAISS vector store for semantic search.

### Retrieval-Augmented Generation Pipeline

* ✅ Created a retriever to perform similarity search over transcript chunks.
* ✅ Built a custom prompt template to ground responses using retrieved context.
* ✅ Implemented an LCEL-based RAG chain:

```
Question
    |
    v
Retriever
    |
    v
Relevant Context
    |
    v
Prompt Template
    |
    v
LLM Response
```

### Chat Interface

* ✅ Added a CLI-based chatbot loop for continuous questions.
* ✅ Implemented streaming responses from the local LLM.
* ✅ Structured the project into separate modules for ingestion, models, indexing, prompts, and chains.

## 🛠️ Current Tech Stack

* **LangChain** - RAG orchestration
* **FAISS** - Vector database
* **Ollama** - Running local LLMs and embedding models
* **Gemma** - Language model
* **EmbeddingGemma** - Embedding model
* **YouTube Transcript API** - Data source

## 📌 Next Learning Goals

* 🔲 Add conversation memory for follow-up questions
* 🔲 Improve retrieval quality with better chunking and retrieval strategies
* 🔲 Add source citations from retrieved documents
* 🔲 Experiment with different embedding models
* 🔲 Build a UI using Streamlit or similar frameworks
