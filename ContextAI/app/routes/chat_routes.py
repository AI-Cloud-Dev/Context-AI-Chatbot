from fastapi import APIRouter, HTTPException, Depends #Request
from app.model.model import ChatRequest, ChatResponse
from app.service.rag_service import get_rag_response
from app.auth.dependencies import get_current_user
# from app.rate_limit.rate_limit import limiter
from app.middleware.rate_limiter import check_rate_limit

router = APIRouter()

@router.post("/chat", response_model=ChatResponse)
# @limiter.limit("2/minute")
def chat_endpoint(
    # request: Request,
    request: ChatRequest,
    user_id: str = Depends(get_current_user)
):
    try:
        check_rate_limit(user_id, "chat")  #Redis Rate Limit
        response_text = get_rag_response(
            user_id=user_id,
            question=request.message
        )

        return ChatResponse(response=response_text)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))