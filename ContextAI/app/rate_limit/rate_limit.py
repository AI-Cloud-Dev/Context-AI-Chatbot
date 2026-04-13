# from fastapi import Request
# from slowapi import Limiter
# from slowapi.util import get_remote_address
# from app.auth.jwt_handler import decode_token

# def get_user_key(request: Request):
#     auth = request.headers.get("Authorization")

#     if auth:
#         parts = auth.split()
#         if len(parts) == 2:
#             token = parts[1]
#             payload = decode_token(token)

#             if payload:
#                 return payload.get("user_id")

#     return get_remote_address(request)

# limiter = Limiter(key_func=get_user_key)