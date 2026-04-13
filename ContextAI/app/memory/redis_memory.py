import redis
import json
from typing import List
from app.model.model import ChatMessage


# connect to Redis

redis_client = redis.Redis(host="localhost", port = 6739, decode_responses = True)

MAX_MESSAGES = 10

def get_memory(user_id: str) -> List[ChatMessage]:
    key = f"chat:{user_id}"
    
    data = redis_client.get(key)
    
    if not data:
        return []
    
    messages_dict = json.loads(data)
    
    return [ChatMessage(**msg) for msg in messages_dict]

def save_memory(user_id: str, messages: List[ChatMessage]):
    key = f"chat:{user_id}"
    
    # Convert to dict
    messages_dict = [msg.dict() for msg in messages]
    
    # Trim memory
    messages_dict = messages_dict[-MAX_MESSAGES:]
    
    redis_client.set(key, json.dumps(messages_dict))