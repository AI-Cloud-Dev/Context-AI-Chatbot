                        🧠 ContextAI — Full-Stack RAG AI Chat System
📌 Overview

ContextAI is a full-stack Retrieval-Augmented Generation (RAG) AI system that allows users to:

Register & login securely (JWT authentication)
Upload documents (PDF, DOCX, XLSX)
Ask questions over uploaded content
Maintain chat memory per user
Enforce rate limiting per user
Get AI-generated responses using local LLM

The system is built with production-grade architecture using FastAPI, Redis, ChromaDB, and Streamlit.

❌ Problem with Traditional Chatbots

Traditional chatbot flow:

User → LLM → Response

Limitations:
No document understanding
No external knowledge injection
No contextual grounding
No persistent memory

✅ Solution: RAG-Based AI System

ContextAI solves this using Retrieval-Augmented Generation (RAG).

User uploads document
        ↓
Extract text (PDF/DOCX/XLSX)
        ↓
Chunk text into smaller sections
        ↓
Generate embeddings
        ↓
Store in vector database (ChromaDB)
        ↓
User asks a question
        ↓
Convert question to embedding
        ↓
Retrieve relevant chunks
        ↓
Send context + question to LLM
        ↓
Generate grounded response

🧠 System Architecture
  
                    ┌──────────────────────┐
                    │   Streamlit UI       │
                    │  (Frontend Layer)    │
                    └──────────┬───────────┘
                               │ JWT Auth API Calls
                               ▼
                    ┌──────────────────────┐
                    │   FastAPI Backend    │
                    │  (Core Engine)       │
                    └──────────┬───────────┘
                               │
        ┌──────────────────────┼──────────────────────┐
        │                      │                      │
        ▼                      ▼                      ▼
┌──────────────┐    ┌──────────────────┐   ┌────────────────────┐
│ JWT Auth     │    │ Redis Layer      │   │ Chroma Vector DB   │
│ Security     │    │ - Chat Memory    │   │ - Embeddings       │
│              │    │ - Rate Limiting  │   │ - Semantic Search  │
└──────────────┘    └──────────────────┘   └────────────────────┘
                               │                      │
                               └──────────┬───────────┘
                                          ▼
                              ┌──────────────────────┐
                              │   Ollama LLM         │
                              │ (Response Generator) │
                              └──────────────────────┘                          

                              
🧰 Tech Stack

FastAPI (Backend API)
Streamlit (Frontend UI)
JWT (Authentication)
Redis (Memory + Rate Limiting)
ChromaDB (Vector Database)
Ollama (LLM inference)
Sentence Transformers (Embeddings)
Python (Core logic)
🔐 Authentication System
JWT-based authentication
Secure login/register flow
Token stored in frontend session
Protects all API endpoints
Ensures user isolation

🧠 Memory System (Redis)

Used for chat memory:

chat:{user_id}

Stores:

conversation history
last N messages only (memory trimming)

Benefits:

fast access
distributed storage
session persistence

⚡ Rate Limiting (Redis-Based)

Implements per-user request control:

rate:chat:{user_id}

Features:

limits API abuse
protects LLM cost
prevents system overload
configurable per endpoint

📚 Document Processing Pipeline
File upload (PDF/DOCX/XLSX)
Extract raw text
Clean text
Chunk text into small sections
Generate embeddings
Store in ChromaDB with metadata

🔍 RAG Pipeline (Core Logic)
User asks a question
Convert question to embedding
Search similar chunks in ChromaDB
Retrieve top-k relevant context
Combine context + chat memory
Send to LLM
Return grounded response

🧠 Key Components

1. Streamlit Frontend
Login/Register UI
Chat interface (ChatGPT style)
File upload UI
API communication layer

2. FastAPI Backend
Auth system
Chat API
Upload API
RAG orchestration

3. Redis Layer
Chat memory storage
Rate limiting system

4. Chroma Vector DB
Stores embeddings
Enables semantic search
Multi-user isolation using metadata

5. LLM (Ollama)
Generates final answers
Uses retrieved context dynamically
Does NOT train on data

🚀 Deployment Architecture

Streamlit Frontend
        ↓
FastAPI Backend (Deployed)
        ↓
Redis (Memory + Rate Limit)
        ↓
ChromaDB (Vector Storage)
        ↓
Ollama LLM

📦 Features

✔ Secure authentication (JWT)
✔ Document upload support
✔ RAG-based question answering
✔ Chat memory per user
✔ Rate limiting protection
✔ Multi-user isolation
✔ Semantic search over documents
✔ Full-stack UI with Streamlit

🧠 Key Learnings

Retrieval-Augmented Generation (RAG)
Vector database usage (ChromaDB)
Embedding-based search
Redis for distributed memory
Rate limiting using Redis
JWT authentication flow
Full-stack AI system design
LLM integration using Ollama

📌 Important Insight

ContextAI does NOT train the LLM on documents.
Instead, it retrieves relevant context dynamically and injects it into prompts.

👨‍💻 Project Flow Summary

User → Streamlit UI → FastAPI → Redis → ChromaDB → Ollama → Response

🏁 Conclusion

ContextAI is a production-ready AI system demonstrating:

Backend engineering
AI system design
Scalable architecture
LLM integration
Real-world RAG implementation

🚀 Author

Built as a full-stack AI engineering project focused on:

LLM application development
RAG systems
Cloud-ready backend architecture
Production-grade AI systems
