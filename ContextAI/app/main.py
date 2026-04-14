import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.chat_routes import router as chat_router
from app.routes.upload_routes import router as upload_router
from app.auth.auth_routes import router as auth_router

# ---------------- APP INIT ----------------
app = FastAPI(title="ContextAI Chatbot")

# ---------------- CORS ----------------
# ✅ CORS must be added BEFORE routes, not after
ALLOWED_ORIGINS = os.environ.get("ALLOWED_ORIGINS", "*").split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,  # set ALLOWED_ORIGINS env var in Render
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------- ROUTES ----------------
app.include_router(chat_router, prefix="/api")
app.include_router(upload_router, prefix="/api")
app.include_router(auth_router, prefix="/auth")

# ---------------- ROOT ----------------
@app.get("/")
def read_root():
    return {"message": "ContextAI API is running 🚀"}

# ---------------- RUN LOCALLY ONLY ----------------
if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)
