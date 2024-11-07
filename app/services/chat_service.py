from langchain_openai import ChatOpenAI
from app.config.settings import settings
from app.models.chat import Message, ChatResponse
from app.services.rag_service import RAGService
from app.templates.chat_prompts import (
    THERAPIST_SYSTEM_PROMPT,
    CHAT_TEMPLATE,
    should_suggest_diary
)
from app.core.logger import logger
from typing import List

class ChatService:
    def __init__(self):
        self.llm = ChatOpenAI(
            model_name=settings.MODEL_NAME,
            openai_api_key=settings.OPENAI_API_KEY,
            temperature=0.7
        )
        self.rag_service = RAGService()
        
    async def get_chat_response(self, messages: List[Message], user_id: str) -> ChatResponse:
        try:
            last_message = next(msg for msg in reversed(messages) if msg.role == "user")
            relevant_contexts = await self.rag_service.find_relevant_context(last_message.content)
            
            chat_history = "\n".join([
                f"{'내담자' if msg.role == 'user' else '상담사'}: {msg.content}" 
                for msg in messages[-settings.CHAT_HISTORY_LENGTH:]
            ])
            
            prompt = THERAPIST_SYSTEM_PROMPT + "\n" + CHAT_TEMPLATE.format(
                context="\n".join(relevant_contexts) if relevant_contexts else "관련 컨텍스트 없음",
                chat_history=chat_history,
                user_message=last_message.content
            )
            
            response = await self.llm.ainvoke(prompt)
            response_text = response.content if hasattr(response, 'content') else str(response)
            
            suggest_diary = should_suggest_diary(
                [msg.content for msg in messages if msg.role == "user"]
            )
            
            return ChatResponse(
                response=response_text,
                suggested_diary=suggest_diary
            )
            
        except Exception as e:
            logger.error(f"Error generating chat response: {str(e)}")
            raise