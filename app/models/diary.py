from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

class DiaryEntry(BaseModel):
    user_id: str
    content: str
    mood: str
    timestamp: datetime = datetime.now()

class DiaryGeneration(BaseModel):
    user_id: str
    chat_history: List[str]