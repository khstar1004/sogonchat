from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv
import os

load_dotenv()

class Settings(BaseSettings):
    # 환경 변수에서 가져올 설정들을 명시적으로 선언
    API_V1_STR: str = "/api"
    PROJECT_NAME: str = "sogon Chatbot API"
    MODEL_NAME: str = "gpt-4o-mini"
    CHAT_HISTORY_LENGTH: int = 5
    DATA_PATH: str = "app/data/chat_diary_dataset.json"
    
    # OpenAI 설정
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")
    
    # Supabase 설정
    SUPABASE_URL: str = os.getenv("SUPABASE_URL", "")
    SUPABASE_KEY: str = os.getenv("SUPABASE_KEY", "")

    # Pydantic v2 설정
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding='utf-8',
        case_sensitive=True,
        extra='allow'  # 추가 필드 허용
    )

settings = Settings() 