import redis
from fastapi import HTTPException


redis_client = redis.Redis(host = "localhost", port = 6379, decode_responses = True)

MAX_REQUESTS = 5
WINDOW_SECONDS = 60

def check_rate_limit(user_id: str, endpoint: str ="chat"):
    key = f"rate:{endpoint}:{user_id}"
    
    count = redis_client.incr(key)
    
    if count == 1:
        redis_client.expire(key, WINDOW_SECONDS)
        
    if count > MAX_REQUESTS:
        raise HTTPException(
            status_code=429,
            detail="Rate Limit exceeded. Try again Later."
        )
