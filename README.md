Contextual RAG Pipeline Prototype
Objective
Building a Retrieval-Augmented Generation (RAG) prototype to evaluate the advantages of using a graph-based multi-model database over standalone vector databases. The goal is to provide better, highly-structured context to LLM prompts by combining vector search with graph relations.

Tech Stack
Database: ArangoDB

Language: Python

AI Framework: LangChain

Environment: Docker

Current Status: Work in Progress 🚧
[x] Initialize ArangoDB connection via Python driver

[x] Set up document collections for vector storage

[ ] Implement LangChain integration

[ ] Benchmark against standalone vector search

How to Run (Local Dev)
Bash
# Install dependencies
pip install -r requirements.txt

# Run the setup script
python main.py
