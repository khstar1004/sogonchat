from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from app.config.settings import settings
from app.core.logger import logger
import json
from typing import List

class RAGService:
    def __init__(self):
        self.embeddings = OpenAIEmbeddings(openai_api_key=settings.OPENAI_API_KEY)
        self.vector_store = None
        self.initialize_vector_store()

    def initialize_vector_store(self) -> None:
        try:
            with open(settings.DATA_PATH, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            text_splitter = RecursiveCharacterTextSplitter(
                chunk_size=1000,
                chunk_overlap=200,
                separators=["\n\n", "\n", ".", "!", "?", ","]
            )
            
            texts = []
            metadatas = []
            
            for entry in data.get('diary_entries', []):
                chunks = text_splitter.split_text(entry['diary_content'])
                texts.extend(chunks)
                emotion = entry.get('emotions', ['neutral'])[0]
                metadatas.extend([{
                    'date': entry.get('date', ''),
                    'emotion': emotion
                } for _ in chunks])
            
            if texts:
                self.vector_store = FAISS.from_texts(
                    texts=texts,
                    embedding=self.embeddings,
                    metadatas=metadatas
                )
                logger.info("Vector store initialized successfully")
            else:
                logger.warning("No texts found to initialize vector store")
            
        except Exception as e:
            logger.error(f"Failed to initialize vector store: {str(e)}")
            raise

    async def find_relevant_context(self, query: str, k: int = 3) -> List[str]:
        try:
            if not self.vector_store:
                logger.warning("Vector store not initialized")
                return []
            
            results = self.vector_store.similarity_search(query, k=k)
            return [doc.page_content for doc in results]
            
        except Exception as e:
            logger.error(f"Error finding relevant context: {str(e)}")
            return []