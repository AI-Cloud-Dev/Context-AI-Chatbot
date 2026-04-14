import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.chat_routes import router as chat_router
from app.routes.upload_routes import router as upload_router
from app.auth.auth_routes import router as auth_router


# ---------------- APP INIT ----------------
app = FastAPI(title="ContextAI Chatbot")


# ---------------- ROOT ----------------
@app.get("/")
def read_root():
    return {"message": "API is running 🚀"}


# ---------------- ROUTES ----------------
app.include_router(chat_router, prefix="/api")
app.include_router(upload_router, prefix="/api")
app.include_router(auth_router, prefix="/auth")


# ---------------- CORS ----------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # later restrict to frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ---------------- RUN LOCALLY ONLY ----------------
if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 10000))
    uvicorn.run("app.main:app", host="0.0.0.0", port=port, reload=True)
