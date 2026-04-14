                                               🧠 ContextAI — Full-Stack RAG AI Chat System


A production-grade, full-stack AI system that lets users upload documents and have intelligent, context-aware conversations over their own data — powered by RAG, vector search, and local LLM inference.


     📌 Overview
ContextAI solves the core limitation of traditional chatbots: they know nothing about your data.
By combining Retrieval-Augmented Generation (RAG) with a full authentication and memory layer, ContextAI allows users to:

🔐 Register and log in securely (JWT authentication)
📄 Upload documents (PDF, DOCX, XLSX)
💬 Ask natural-language questions over their uploaded content
🧠 Maintain persistent chat memory per user session
⚡ Benefit from per-user rate limiting to protect system resources
🤖 Receive grounded, context-aware AI responses via local LLM (Ollama)


                  🏗️ System Architecture
                  
                  ┌──────────────────────┐
                  │    Streamlit UI      │  ← Frontend layer (chat interface + file upload)
                  └──────────┬───────────┘
                             │ JWT-authenticated API calls
                             ▼
                  ┌──────────────────────┐
                  │   FastAPI Backend    │  ← Core engine (auth, RAG orchestration, APIs)
                  └──────────┬───────────┘
                             │
                  ┌──────────┼──────────────────────┐
                  ▼          ▼                      ▼
    ┌──────────────┐  ┌────────────────────┐  ┌──────────────────────┐
    │  JWT Auth    │  │   Redis Layer      │  │  ChromaDB            │
    │  Security   │  │  - Chat memory     │  │  - Embeddings        │
    │             │  │  - Rate limiting   │  │  - Semantic search   │
    └──────────────┘  └────────────────────┘  └──────────────────────┘
                               │                        │
                               └──────────┬─────────────┘
                                          ▼
                              ┌──────────────────────┐
                              │   Ollama (Local LLM) │  ← Generates grounded responses
                              └──────────────────────┘


✨ Features
FeatureDetails🔐 JWT AuthenticationSecure register/login, token-protected endpoints, user isolation📄 Document UploadSupports PDF, DOCX, XLSX with text extraction pipeline🧠 RAG PipelineChunk → Embed → Store → Retrieve → Generate💬 Chat MemoryPer-user conversation history stored in Redis⚡ Rate LimitingRedis-based per-user request throttling🔍 Semantic SearchEmbedding-based document retrieval via ChromaDB🤖 Local LLMOllama inference — no external API costs🖥️ Full-Stack UIChatGPT-style Streamlit interface

    🛠️ Tech Stack
LayerTechnologyFrontendStreamlitBackend APIFastAPIAuthenticationJWT (JSON Web Tokens)Memory & Rate LimitingRedisVector DatabaseChromaDBEmbeddingsSentence TransformersLLM InferenceOllama (local)LanguagePython 3.11

    🚀 Getting Started
Prerequisites

Python 3.10+
Redis running locally (redis-server)
Ollama installed and running (ollama run llama3)
(Optional) Docker

1. Clone the repository
bashgit clone https://github.com/AI-Cloud-Dev/Context-AI-Chatbot.git
cd Context-AI-Chatbot
2. Create and activate a virtual environment
bashpython -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
3. Install dependencies
bashpip install -r requirements.txt
4. Set up environment variables
bashcp .env.example .env
# Edit .env with your settings (JWT secret, Redis URL, etc.)
5. Start the FastAPI backend
bashcd ContextAI
uvicorn main:app --reload --port 8000
6. Start the Streamlit frontend
bashstreamlit run app.py
Open your browser at http://localhost:8501

        📁 Project Structure
        Context-AI-Chatbot/
        ├── ContextAI/
        │   ├── main.py              # FastAPI app entry point
        │   ├── auth.py              # JWT authentication logic
        │   ├── rag.py               # RAG pipeline (embed, retrieve, generate)
        │   ├── memory.py            # Redis chat memory management
        │   ├── rate_limiter.py      # Redis-based rate limiting
        │   ├── document_parser.py   # PDF/DOCX/XLSX text extraction
        │   └── vector_store.py      # ChromaDB integration
        ├── app.py                   # Streamlit frontend
        ├── requirements.txt
        ├── .env.example
        └── README.md

🔄 RAG Pipeline — How It Works

    1. User uploads document (PDF/DOCX/XLSX)
            ↓
    2. Extract and clean raw text
            ↓
    3. Chunk text into semantic segments
            ↓
    4. Generate embeddings (Sentence Transformers)
            ↓
    5. Store embeddings in ChromaDB (with user metadata)
            ↓
    6. User asks a question
            ↓
    7. Convert question to embedding
            ↓
    8. Retrieve top-k relevant chunks from ChromaDB
            ↓
    9. Combine: retrieved context + chat history (from Redis)
            ↓
    10. Send enriched prompt to Ollama LLM
            ↓
    11. Return grounded, context-aware response

⚠️ Important: ContextAI does not fine-tune or train the LLM on your documents. It dynamically retrieves relevant context at query time and injects it into the prompt — keeping inference fast and the model stateless.


    🧠 Key Design Decisions

Why Redis for memory? Fast in-memory access, distributed-ready, and supports TTL-based session expiry natively.
Why ChromaDB? Lightweight, embeddable vector store with metadata filtering — ideal for per-user document isolation without running a full vector DB server.
Why Ollama (local LLM)? Zero API costs, full data privacy, and easy model swapping (Llama 3, Mistral, Phi-3, etc.).

    📖 Key Learnings

Designing production-grade RAG pipelines from scratch
Multi-user isolation in vector databases using metadata filtering
Redis patterns for distributed memory and rate limiting
JWT authentication integrated with FastAPI dependency injection
Building full-stack AI systems with a clean separation of concerns


    🗺️ Roadmap

 Add streaming responses (FastAPI + Streamlit SSE)
 Docker Compose setup for one-command deployment
 LangSmith observability integration
 AWS deployment guide (EC2 + S3 for document storage)
 Support for web URL ingestion (scrape + embed)


                                                                 👩‍💻 Author
Sreeja — Mid-Level AI Engineer
🔗 GitHub | LinkedIn | Portfolio

📄 License
MIT License — 
