from sentence_transformers import SentenceTransformer
import numpy as np


# Load model once
model = SentenceTransformer("all-MiniLM-L6-v2")

def get_embedding(text: str):
    if not isinstance(text, str):
        raise ValueError(f"Expected string, got {type(text)}")

    embedding = model.encode(text)

    # 🔥 Ensure correct format
    embedding = embedding.tolist()

    if not isinstance(embedding, list):
        raise ValueError("Embedding is not a list")

    return embedding