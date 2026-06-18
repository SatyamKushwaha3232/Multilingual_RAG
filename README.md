<div align="center">

# 🌍 Multilingual RAG System  
### AI-Powered Document Intelligence with Multilingual Question Answering

<p>
  <img src="https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python" />
  <img src="https://img.shields.io/badge/FastAPI-Backend-009688?style=for-the-badge&logo=fastapi" />
  <img src="https://img.shields.io/badge/Groq-LLM-black?style=for-the-badge" />
  <img src="https://img.shields.io/badge/ChromaDB-Vector_DB-orange?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Docker-Containerized-2496ED?style=for-the-badge&logo=docker" />
  <img src="https://img.shields.io/badge/Hugging_Face-Live-yellow?style=for-the-badge&logo=huggingface" />
</p>

<p>
  <b>Upload documents, ask questions in multiple languages, and get context-aware AI answers using RAG.</b>
</p>

<p>
  <a href="https://huggingface.co/spaces/Satyamkushwaha3232/multilingual-rag">
    <img src="https://img.shields.io/badge/🚀_Live_Demo-Hugging_Face-yellow?style=for-the-badge" />
  </a>
  <a href="https://github.com/SatyamKushwaha3232/Multilingual_RAG/releases/tag/v1.0.1">
    <img src="https://img.shields.io/badge/Release-v1.0.1-green?style=for-the-badge" />
  </a>
</p>

</div>

---

## 📌 About The Project

**Multilingual RAG System** is an AI-powered document question-answering application built using **Retrieval-Augmented Generation (RAG)**.

Users can upload documents and ask questions in different languages. The system retrieves the most relevant document chunks using semantic search and generates accurate answers using **Groq LLM**.

This project demonstrates practical implementation of:

- Retrieval-Augmented Generation
- Vector Databases
- Semantic Search
- FastAPI APIs
- Docker Deployment
- Hugging Face Spaces Hosting
- Multilingual AI Applications

---

## ✨ Features

| Feature | Description |
|---|---|
| 📄 PDF Upload | Upload document files for AI-based question answering |
| 🌍 Multilingual QA | Ask questions in multiple languages |
| 🧠 RAG Pipeline | Retrieves document context before generating answers |
| 🔎 Semantic Search | Finds relevant chunks using embeddings |
| 📚 ChromaDB | Stores and searches vector embeddings |
| ⚡ Groq LLM | Generates fast contextual AI responses |
| 🚀 FastAPI | Backend API built with FastAPI |
| 🐳 Docker | Containerized deployment |
| 🤗 Hugging Face | Public live deployment |

---

## 🛠 Tech Stack

### Backend
- Python
- FastAPI
- Uvicorn

### AI / NLP
- Groq LLM
- Sentence Transformers
- LangDetect
- Deep Translator

### Vector Database
- ChromaDB

### Frontend
- HTML
- CSS
- JavaScript

### Deployment
- Docker
- Hugging Face Spaces
- GitHub

---

## 🧠 Architecture

```txt
User
 │
 ▼
Frontend UI
 │
 ▼
FastAPI Backend
 │
 ▼
Document Processor
 │
 ▼
Text Chunking
 │
 ▼
Sentence Transformer Embeddings
 │
 ▼
ChromaDB Vector Store
 │
 ▼
Semantic Retriever
 │
 ▼
Groq LLM
 │
 ▼
Final Context-Aware Answer

1. User uploads PDF
2. Backend extracts text
3. Text is split into chunks
4. Chunks are converted into embeddings
5. Embeddings are stored in ChromaDB
6. User asks a question
7. Relevant chunks are retrieved
8. Groq LLM generates answer using retrieved context
9. Answer is displayed with source references

📂 Folder Structure
Multilingual_RAG/
│
├── backend/
│   ├── main.py
│   ├── rag_engine.py
│   ├── embeddings.py
│   ├── vector_store.py
│   ├── translator.py
│   └── document_processor.py
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── Dockerfile
├── requirements.txt
├── .dockerignore
├── .env.example
└── README.md

🚀 Live Demo

🌍 Live Project:
https://huggingface.co/spaces/Satyamkushwaha3232/multilingual-rag

💻 GitHub Repository:
https://github.com/SatyamKushwaha3232/Multilingual_RAG

⚙️ Local Setup
1. Clone Repository
git clone https://github.com/SatyamKushwaha3232/Multilingual_RAG.git
cd Multilingual_RAG

2. Create Virtual Environment
python -m venv venv
3. Activate Virtual Environment
Windows:
venv\Scripts\activate
Linux/Mac:
source venv/bin/activate

4. Install Dependencies
pip install -r requirements.txt

5. Add Environment Variable
Create .env file:
GROQ_API_KEY=your_groq_api_key_here

6. Run App
uvicorn backend.main:app --reload
Open:
http://localhost:8000

🐳 Docker Setup

Build Docker image:
docker build -t multilingual-rag .

Run container:
docker run -p 7860:7860 multilingual-rag

Open:
http://localhost:7860

🔐 Environment Variables
Variable	Purpose
GROQ_API_KEY	Used to connect Groq LLM
GEMINI_API_KEY	Optional fallback key

💡 Example Questions
What is memory organization?
Explain cache memory in simple language.
Memory Organization kya hai?
Summarize this document.
Explain this topic in Hindi.

📌 Key Learnings

Through this project, I learned:

How RAG systems work
How embeddings are created
How vector databases store semantic meaning
How FastAPI handles backend APIs
How Docker helps in deployment
How to deploy AI apps on Hugging Face Spaces
How to migrate from Gemini to Groq
How to debug real-world deployment issues

🏷 Release

Latest Release:
v1.0.1

Release includes:
PDF Upload
RAG Pipeline
ChromaDB Vector Search
Groq LLM Integration
FastAPI Backend
Docker Deployment
Hugging Face Hosting

🔮 Future Roadmap
 Multiple PDF Upload
 Chat History
 Page Number Citations
 OCR Support
 Voice Input
 Voice Output
 Authentication
 Admin Dashboard
 Cloud Database
 Advanced Analytics
 Streaming Responses
 Custom Domain

🧑‍💻 Author
<div align="center">
Satyam Kushwaha

Aspiring Software Engineer | Full Stack Developer | AI Enthusiast

<p> <a href="https://github.com/SatyamKushwaha3232"> <img src="https://img.shields.io/badge/GitHub-SatyamKushwaha3232-black?style=for-the-badge&logo=github" /> </a> <a href="https://huggingface.co/spaces/Satyamkushwaha3232/multilingual-rag"> <img src="https://img.shields.io/badge/Live_Demo-Hugging_Face-yellow?style=for-the-badge&logo=huggingface" /> </a> </p> </div>
⭐ Support

If you like this project, please give it a ⭐ on GitHub.

It motivates me to build more AI-powered open-source projects.

<div align="center">
Made with ❤️ by Satyam Kushwaha
</div> ```

