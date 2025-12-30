from typing import Optional
from sqlmodel import Field
from app.models.base import BaseEntity

class Conversation(BaseEntity, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: str = Field(index=True)

class Message(BaseEntity, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    conversation_id: int = Field(foreign_key="conversation.id")
    user_id: str
    role: str # user, assistant
    content: str
