from fastapi import FastAPI
from app.routes.chat_routes import router as chat_router
from app.routes.upload_routes import router as upload_router
from app.auth.auth_routes import router as auth_router
# # from slowapi import Limiter
# from slowapi.middleware import SlowAPIMiddleware
# from slowapi.util import get_remote_address
# # from slowapi.errors import RateLimitExceeded
# from fastapi.responses import JSONResponse
# from app.rate_limit.rate_limit import limiter
# from fastapi import Request


app = FastAPI()

# app.state.limiter = limiter
# limiter = Limiter(key_func = get_remote_address)

app.include_router(chat_router, prefix = "/api")
app.include_router(upload_router, prefix= "/api")
app.include_router(auth_router, prefix = "/auth")

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # later restrict
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# app.add_middleware(SlowAPIMiddleware)

# @app.exception_handler(RateLimitExceeded)
# def rate_limit_handler(request, exc: RateLimitExceeded):
#     return JSONResponse(
#         status_code=429,
#         content = {"detail": "Too many requests. Please try again later"}
#     )