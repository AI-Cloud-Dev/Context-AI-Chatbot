
import chromadb
from typing import List
import uuid

_client = None
_collection = None


def get_collection():
    global _client, _collection

    if _collection is None:
        _client = chromadb.PersistentClient(path="./chroma-db")
        _collection = _client.get_or_create_collection(name="documents")

    return _collection


def add_documents(user_id: str, chunks: List[str], embeddings: List[List[float]]):

    if len(chunks) != len(embeddings):
        raise ValueError("Chunks and embeddings length mismatch")

    if not chunks:
        return

    collection = get_collection()

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
        documents=chunks,
        embeddings=embeddings,
        metadatas=metadatas
    )


def search_documents(user_id: str, query_embedding: List[float], k: int = 3):

    collection = get_collection()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=k,
        where={"user_id": user_id}
    )

    docs = results.get("documents")

    if not docs:
        return []

    return docs[0]


def delete_user_docs(user_id: str):
    collection = get_collection()
    collection.delete(where={"user_id": user_id})



# import chromadb
# from typing import List
# import uuid


# chroma_client = chromadb.PersistentClient(path = "./chroma-db")

# # SINGLE COLLECTION
# collection = chroma_client.get_or_create_collection(name = "documents")



# def add_documents(user_id, chunks: List[str], embeddings: List[List[float]]):
    
#     """
#     Store document chunks + embeddings in ChromaDB
#     """

#     # 🔒 Safety checks (IMPORTANT)
#     if len(chunks) != len(embeddings):
#         raise ValueError("Chunks and embeddings length mismatch")

#     if len(chunks) == 0:
#         return

    
#     ids = []
#     metadatas = []
    
#     for i in range(len(chunks)):
#         ids.append(str(uuid.uuid4()))
        
#         metadatas.append({
#             "user_id": user_id,
#             "chunk_index": i
#         })
    
#     collection.add(
#         ids=ids,
#         documents = chunks,
#         embeddings = embeddings,
#         metadatas = metadatas
#     )

# def search_documents(user_id:str, query_embedding: list, k: int = 3):
    
#     results = collection.query(
#         query_embeddings = [query_embedding],
#         n_results = k,
#         where = {"user_id": user_id} 
#     )
    
#     return results.get("documents",[[]])[0]

# def delete_user_docs(user_id: str):
#     """
#     Optional helper: delete all documents for a user
#     """
#     collection.delete(where={"user_id": user_id})
