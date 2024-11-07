from supabase import create_client, Client
from app.config.settings import settings
from app.core.logger import logger
from typing import Dict, List, Optional
from datetime import datetime

class Database:
    def __init__(self):
        try:
            if not settings.SUPABASE_URL or not settings.SUPABASE_KEY:
                raise ValueError("Supabase credentials not properly configured")
                
            self.client: Client = create_client(
                supabase_url=settings.SUPABASE_URL,
                supabase_key=settings.SUPABASE_KEY
            )
            logger.info("Successfully connected to Supabase")
        except Exception as e:
            logger.error(f"Failed to initialize Supabase client: {str(e)}")
            raise

    async def save_chat_message(self, message: Dict) -> Dict:
        try:
            result = self.client.table('chat_messages').insert(message).execute()
            return result.data[0]
        except Exception as e:
            logger.error(f"Error saving chat message: {str(e)}")
            raise

    async def get_chat_history(self, user_id: str) -> List[Dict]:
        try:
            result = self.client.table('chat_messages')\
                .select('*')\
                .eq('user_id', user_id)\
                .order('timestamp', desc=True)\
                .limit(settings.CHAT_HISTORY_LENGTH)\
                .execute()
            return result.data
        except Exception as e:
            logger.error(f"Error fetching chat history: {str(e)}")
            raise

    async def save_diary(self, diary: Dict) -> Dict:
        try:
            result = self.client.table('diary_entries').insert(diary).execute()
            return result.data[0]
        except Exception as e:
            logger.error(f"Error saving diary: {str(e)}")
            raise

    async def get_diary_history(self, user_id: str) -> List[Dict]:
        try:
            result = self.client.table('diary_entries')\
                .select('*')\
                .eq('user_id', user_id)\
                .order('timestamp', desc=True)\
                .execute()
            return result.data
        except Exception as e:
            logger.error(f"Error fetching diary history: {str(e)}")
            raise

db = Database() 