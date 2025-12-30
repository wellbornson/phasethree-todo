from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from typing import Optional, List
from sqlmodel import Session
from app.agents.runner import get_agent
from app.core.db import get_session
from app.services.history import HistoryService
import traceback

router = APIRouter()

class ChatRequest(BaseModel):
    message: str
    conversation_id: Optional[int] = None

class ChatResponse(BaseModel):
    conversation_id: int
    response: str
    tool_calls: List[dict] = []

@router.post("/{user_id}/chat", response_model=ChatResponse)
async def chat_endpoint(user_id: str, request: ChatRequest, session: Session = Depends(get_session)):
    try:
        history_svc = HistoryService(session)
        
        previous_messages = []
        if request.conversation_id:
            conversation = history_svc.get_conversation(request.conversation_id, user_id)
            if not conversation:
                raise HTTPException(status_code=404, detail="Conversation not found")
            conv_id = conversation.id
            previous_messages = history_svc.get_messages(conv_id)
        else:
            conversation = history_svc.create_conversation(user_id)
            conv_id = conversation.id

        # Store user message
        history_svc.add_message(conv_id, user_id, "user", request.message)

        agent = get_agent(user_id)
        # Pass history (previous_messages) to the agent
        result = await agent.run(request.message, history=previous_messages)

        # Store assistant response
        if result.content:
            history_svc.add_message(conv_id, user_id, "assistant", result.content)
        
        return ChatResponse(
            conversation_id=conv_id,
            # Handle case where content might be None (pure tool call, though we handle that in runner loop)
            response=result.content or "", 
            tool_calls=result.tool_calls
        )
    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))