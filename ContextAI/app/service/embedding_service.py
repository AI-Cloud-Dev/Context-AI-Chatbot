from sentence_transformers import SentenceTransformer

_model = None

def get_model():
    global _model
    if _model is None:
        print("Loading embedding model...")
        from sentence_transformers import SentenceTransformer  # 👈 move here
        _model = SentenceTransformer("all-MiniLM-L6-v2")
    return _model

# def get_model():
#     global _model
#     if _model is None:
#         print("Loading embedding model...")
#         _model = SentenceTransformer("all-MiniLM-L6-v2")
#     return _model

def get_embedding(text: str):
    if not isinstance(text, str):
        raise ValueError(f"Expected string, got {type(text)}")

    model = get_model()
    embedding = model.encode(text)

    return embedding.tolist()
