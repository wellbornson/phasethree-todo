from sqlmodel import Session, select
from app.models.chat import Conversation, Message
from typing import List, Optional

class HistoryService:
    def __init__(self, session: Session):
        self.session = session

    def get_conversation(self, conversation_id: int, user_id: str) -> Optional[Conversation]:
        return self.session.exec(
            select(Conversation).where(Conversation.id == conversation_id, Conversation.user_id == user_id)
        ).first()

    def create_conversation(self, user_id: str) -> Conversation:
        conv = Conversation(user_id=user_id)
        self.session.add(conv)
        self.session.commit()
        self.session.refresh(conv)
        return conv

    def add_message(self, conversation_id: int, user_id: str, role: str, content: str):
        msg = Message(conversation_id=conversation_id, user_id=user_id, role=role, content=content)
        self.session.add(msg)
        self.session.commit()

    def get_messages(self, conversation_id: int, limit: int = 10) -> List[Message]:
        return self.session.exec(
            select(Message)
            .where(Message.conversation_id == conversation_id)
            .order_by(Message.created_at.desc())
            .limit(limit)
        ).all()[::-1] # Reverse to get chronological order
