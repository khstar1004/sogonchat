from langchain_openai import ChatOpenAI
from app.config.settings import settings
from app.models.diary import DiaryEntry
from app.templates.diary_prompts import (
    DIARY_SYSTEM_PROMPT,
    DIARY_TEMPLATE,
    parse_diary_response
)
from app.core.logger import logger
from typing import List

class DiaryService:
    def __init__(self):
        self.llm = ChatOpenAI(
            model_name=settings.MODEL_NAME,
            openai_api_key=settings.OPENAI_API_KEY,
            temperature=0.7
        )
    
    async def generate_diary(self, chat_history: List[str], user_id: str) -> DiaryEntry:
        try:
            prompt = DIARY_SYSTEM_PROMPT + "\n" + DIARY_TEMPLATE.format(
                chat_history="\n".join(chat_history)
            )
            
            response = await self.llm.ainvoke(prompt)
            response_text = response.content if hasattr(response, 'content') else str(response)
            
            mood, content = parse_diary_response(response_text)
            
            return DiaryEntry(
                user_id=user_id,
                content=content,
                mood=mood
            )
            
        except Exception as e:
            logger.error(f"Error generating diary: {str(e)}")
            raise