# Contextual RAG Pipeline Prototype

A Python-based prototype to evaluate the advantages of using ArangoDB (a graph-based multi-model database) over standalone vector databases. The goal is to provide richer, structured context to LLM prompts by combining vector search with graph relationships.

## Project Overview

Modern Retrieval-Augmented Generation (RAG) pipelines often rely on pure vector search, which can miss complex semantic relationships and hierarchical contexts. This prototype integrates graph structures with vector metadata to query connected data points, enhancing prompt construction.

## Tech Stack

* **Database:** ArangoDB
* **Runtime:** Python 3
* **Libraries:** `python-arango`, `langchain`
* **Infrastructure:** Docker

## Progress Checklist

- [x] Establish ArangoDB client connection
- [x] Create document collections for vector storage
- [ ] Implement LangChain integration for retrieval
- [ ] Benchmark query quality against a standard vector database

## Getting Started

### Prerequisites

Ensure you have a local ArangoDB instance running (default port `8529`). You can quickly spin up an instance using Docker:

```bash
docker run -d -p 8529:8529 -e ARANGO_NO_AUTH=1 arangodb/arangodb:latest
```

### Installation

1. Clone the repository and navigate to the project directory.
2. Install the required Python dependencies:

```bash
pip install -r requirements.txt
```

### Usage

Run the initialization script to connect to the database and set up the initial document collections:

```bash
python main.py
```
