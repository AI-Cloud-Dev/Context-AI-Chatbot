import redis
import json
from typing import List
from app.model.model import ChatMessage
import os


# connect to Redis

REDIS_URL = os.getenv("REDIS_URL")

if not REDIS_URL:
    raise ValueError("REDIS_URL is not set in environment variables")

redis_client = redis.Redis.from_url(
    REDIS_URL,
    decode_responses=True
)

MAX_MESSAGES = 10

def get_memory(user_id: str) -> List[ChatMessage]:

    if not redis_client:
        return []

    key = f"chat:{user_id}"

    try:
        data = redis_client.get(key)
        if not data:
            return []

        messages_dict = json.loads(data)
        return [ChatMessage(**msg) for msg in messages_dict]

    except Exception:
        return []

def save_memory(user_id: str, messages: List[ChatMessage]):

    if not redis_client:
        return

    try:
        key = f"chat:{user_id}"

        messages_dict = [msg.dict() for msg in messages]
        messages_dict = messages_dict[-MAX_MESSAGES:]

        redis_client.set(key, json.dumps(messages_dict))

    except Exception:
        pass
