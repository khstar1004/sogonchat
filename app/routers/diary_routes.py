from fastapi import APIRouter, HTTPException
from app.models.diary import DiaryEntry, DiaryGeneration
from app.services.diary_service import DiaryService
from app.core.database import db
from app.core.logger import logger
from typing import List
from datetime import datetime

router = APIRouter()
diary_service = DiaryService()

@router.post("/generate", response_model=DiaryEntry)
async def generate_diary(request: DiaryGeneration):
    try:
        if not request.chat_history:
            raise HTTPException(
                status_code=400, 
                detail="Chat history cannot be empty"
            )
            
        diary = await diary_service.generate_diary(
            chat_history=request.chat_history,
            user_id=request.user_id
        )
        
        # 생성된 일기 저장
        saved_diary = await db.save_diary({
            "user_id": diary.user_id,
            "content": diary.content,
            "mood": diary.mood,
            "timestamp": diary.timestamp.isoformat()
        })
        
        return DiaryEntry(**saved_diary)
        
    except Exception as e:
        logger.error(f"Error generating diary: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to generate diary")

@router.get("/history/{user_id}", response_model=List[DiaryEntry])
async def get_diary_history(user_id: str):
    try:
        diary_history = await db.get_diary_history(user_id)
        return [
            DiaryEntry(
                user_id=diary["user_id"],
                content=diary["content"],
                mood=diary["mood"],
                timestamp=datetime.fromisoformat(diary["timestamp"])
            )
            for diary in diary_history
        ]
    except Exception as e:
        logger.error(f"Error fetching diary history: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to fetch diary history")
