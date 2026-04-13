import chromadb
from typing import List
import uuid


chroma_client = chromadb.PersistentClient(path = "./chroma-db")

# SINGLE COLLECTION
collection = chroma_client.get_or_create_collection(name = "documents")



def add_documents(user_id, chunks: List[str], embeddings: List[List[float]]):
    
    """
    Store document chunks + embeddings in ChromaDB
    """

    # 🔒 Safety checks (IMPORTANT)
    if len(chunks) != len(embeddings):
        raise ValueError("Chunks and embeddings length mismatch")

    if len(chunks) == 0:
        return

    
    ids = []
    metadatas = []
    
    for i in range(len(chunks)):
        ids.append(str(uuid.uuid4()))
        
        metadatas.append({
            "user_id": user_id,
            "chunk_index": i
        })
    
    collection.add(
        ids=ids,
        documents = chunks,
        embeddings = embeddings,
        metadatas = metadatas
    )

def search_documents(user_id:str, query_embedding: list, k: int = 3):
    
    results = collection.query(
        query_embeddings = [query_embedding],
        n_results = k,
        where = {"user_id": user_id} 
    )
    
    return results.get("documents",[[]])[0]

def delete_user_docs(user_id: str):
    """
    Optional helper: delete all documents for a user
    """
    collection.delete(where={"user_id": user_id})