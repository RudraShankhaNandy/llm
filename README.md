
# Research Paper Management API

## Overview
This project provides an API for managing and querying research papers, powered by FastAPI, Neo4j for data storage, and Transformers for NLP tasks.

## Features
- Store research paper metadata (title, abstract, etc.) in a Neo4j graph database.
- Query and retrieve research papers based on user input.
- Generate summaries, answer questions, and create review papers.

## Project Structure
- `main.py`: Entry point for running the FastAPI server.
- `api.py`: Contains API logic for querying, summarization, and paper management.
- `common/embedder.py`: Embedding generator using Transformers.
- `common/prompts.py`: Constructs prompts for model processing.
- `common/graphdb.py`: Interacts with the Neo4j database.

## Running the Project
### Prerequisites
- Docker and Docker Compose
- Python 3.9 or later

### Steps
1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd project-root
   ```
2. **Create a `.env` file** with the following content:
   ```bash
   HOST=api
   PORT=8080
   NEO4J_URL=bolt://localhost:7687
   NEO4J_USER=neo4j
   NEO4J_PASSWORD=password
   ```
3. **Build and run using Docker Compose**:
   ```bash
   docker-compose up
   ```
4. **Access the API** at `http://localhost:8080`.

## API Endpoints
- `POST /query`: Query stored research papers.
- `POST /store_paper`: Store new research paper data.

## Requirements
Install dependencies using:
```bash
pip install -r requirements.txt
```
#   l l m  
 