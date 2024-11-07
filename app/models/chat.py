from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class Message(BaseModel):
    role: str
    content: str
    timestamp: datetime = datetime.now()

class ChatHistory(BaseModel):
    messages: List[Message]
    user_id: str

class ChatResponse(BaseModel):
    response: str
    suggested_diary: Optional[bool] = False 