# Upwork Technical Support AI Bot (RAG)

## Project Overview

This project is a Retrieval-Augmented Generation (RAG) application developed as part of the **ProAnalyst Associate AI Developer Take-Home Assignment**.

The application answers developer questions about the Upwork API using only the provided technical documentation. It retrieves the most relevant documentation snippets using semantic search and generates responses using a hosted Large Language Model (LLM).

---

## Features

* Load Upwork API PDF documentation
* Perform document sanity check
* Split documentation into chunks (500 characters with 50-character overlap)
* Generate embeddings using Sentence Transformers
* Store embeddings locally using ChromaDB
* Retrieve the Top-3 most relevant chunks
* Generate answers using the provided hosted LLM API
* Hallucination guard to avoid unsupported answers
* Streamlit-based user interface
* Display retrieved source snippets
* Display response latency

---

## Technologies Used

* Python (3.11)
* LangChain
* ChromaDB
* Sentence Transformers
* Streamlit
* Requests
* DeepInfra Hosted API

---

## Project Structure

```text
Associate-AI-Developer/
│
├── app.py
├── build_vector_db.py
├── config.py
├── requirements.txt
├── README.md
├── Technical_Summary.md
├── .env.example
│
├── data/
├── db/
├── ingestion/
├── rag/
└── utils/
```

---

## Installation

### Clone the repository

```bash
git clone <repository-url>
```

### Create Virtual Environment

```bash
python -m venv venv
```

Activate it.

Windows:

```bash
venv\Scripts\activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

### Configure Environment Variables

Create a `.env` file using `.env.example`.

Example:

```text
DEEPINFRA_API_KEY=YOUR_API_KEY
MODEL_NAME=meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo
```

---

## Build Vector Database

```bash
python build_vector_db.py
```

---

## Run the Application

```bash
streamlit run app.py
```

---

## Workflow

1. Load PDF documentation.
2. Split the document into overlapping chunks.
3. Generate embeddings.
4. Store vectors in ChromaDB.
5. Retrieve the Top-3 relevant chunks.
6. Send retrieved context to the hosted LLM.
7. Display answer, sources, and response latency.

---

## Assignment Evaluation Questions

The application is designed to answer the following questions using only the provided documentation:

1. What is the specific request-per-second rate limit for the Upwork API, and is it enforced per Key or per IP?
2. How long is an OAuth access token valid for?
3. Can I use a Client Credentials Grant to access a user's private contract details?

---

## Notes

* The application only answers using the provided documentation.
* If the required information is unavailable, the assistant returns the predefined hallucination guard response.
* API keys are stored securely using environment variables.
