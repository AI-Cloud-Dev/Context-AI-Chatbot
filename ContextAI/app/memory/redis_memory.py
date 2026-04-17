import redis
import json
import os
from typing import List, Optional
from app.model.model import ChatMessage

# ---------------------------
# CONFIG
# ---------------------------

REDIS_URL = os.getenv("REDIS_URL")

redis_client: Optional[redis.Redis] = None

if REDIS_URL:
    try:
        redis_client = redis.Redis.from_url(
            REDIS_URL,
            decode_responses=True,
            socket_connect_timeout=5,
            socket_timeout=5
        )
        # test connection
        redis_client.ping()
        print("Redis connected successfully")
    except Exception as e:
        print(f"Redis connection failed: {e}")
        redis_client = None
else:
    print("REDIS_URL not found, running without Redis")


MAX_MESSAGES = 10


# ---------------------------
# GET MEMORY
# ---------------------------
def get_memory(user_id: str) -> List[ChatMessage]:

    if redis_client is None:
        return []

    try:
        key = f"chat:{user_id}"
        data = redis_client.get(key)

        if not data:
            return []

        messages_dict = json.loads(data)

        return [
            ChatMessage(**msg) for msg in messages_dict
        ]

    except Exception as e:
        print(f"Redis read error: {e}")
        return []


# ---------------------------
# SAVE MEMORY
# ---------------------------
def save_memory(user_id: str, messages: List[ChatMessage]):

    if redis_client is None:
        return

    try:
        key = f"chat:{user_id}"

        # keep only last N messages
        trimmed = messages[-MAX_MESSAGES:]

        data = [msg.dict() for msg in trimmed]

        redis_client.set(
            key,
            json.dumps(data),
            ex=3600  # 1 hour expiry (important for memory control)
        )

    except Exception as e:
        print(f"Redis write error: {e}")


# import redis
# import json
# from typing import List
# from app.model.model import ChatMessage
# import os


# # connect to Redis

# REDIS_URL = os.getenv("REDIS_URL")

# if not REDIS_URL:
#     raise ValueError("REDIS_URL is not set in environment variables")

# redis_client = redis.Redis.from_url(
#     REDIS_URL,
#     decode_responses=True
# )

# MAX_MESSAGES = 10

# def get_memory(user_id: str) -> List[ChatMessage]:

#     if not redis_client:
#         return []

#     key = f"chat:{user_id}"

#     try:
#         data = redis_client.get(key)
#         if not data:
#             return []

#         messages_dict = json.loads(data)
#         return [ChatMessage(**msg) for msg in messages_dict]

#     except Exception:
#         return []

# def save_memory(user_id: str, messages: List[ChatMessage]):

#     if not redis_client:
#         return

#     try:
#         key = f"chat:{user_id}"

#         messages_dict = [msg.dict() for msg in messages]
#         messages_dict = messages_dict[-MAX_MESSAGES:]

#         redis_client.set(key, json.dumps(messages_dict))

#     except Exception:
#         pass
# /
