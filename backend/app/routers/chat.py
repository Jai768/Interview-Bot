from fastapi import APIRouter
from backend.app.services.llm import groq_chat_completion
from backend.app.schemas.ai_service import ChatRequest
import uuid

router = APIRouter()

@router.get("/start_session")
async def start_session():
    session_id = str(uuid.uuid4())
    return {"session_id": session_id}

@router.post("/chat")
async def send_message(request: ChatRequest):
    response = groq_chat_completion(request.session_id, request.message)
    return {"response": response}