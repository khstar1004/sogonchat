from fastapi import APIRouter, HTTPException

from app.models.chat import Message, ChatHistory, ChatResponse

from app.services.chat_service import ChatService

from app.core.logger import logger

from typing import List

from datetime import datetime

router = APIRouter()

chat_service = ChatService()

@router.post("/message", response_model=ChatResponse)
async def send_message(chat_history: ChatHistory):
    try:
        if not chat_history.messages:
            raise HTTPException(status_code=400, detail="Chat history cannot be empty")

        response = await chat_service.get_chat_response(
            messages=chat_history.messages,
            user_id=chat_history.user_id
        )

        return response

    except StopIteration:
        logger.error("StopIteration occurred in coroutine")
        raise HTTPException(status_code=500, detail="Internal server error")
    except Exception as e:
        logger.error(f"Error processing message: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to process message")

@router.post("/diary/generate", response_model=ChatResponse)
async def generate_diary(chat_history: ChatHistory):
    try:
        if not chat_history.messages:
            raise HTTPException(status_code=400, detail="Chat history cannot be empty")

        # Assuming the chat_service can also handle diary generation
        response = await chat_service.get_chat_response(
            messages=chat_history.messages,
            user_id=chat_history.user_id
        )

        return response

    except Exception as e:
        logger.error(f"Error generating diary: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to generate diary")
