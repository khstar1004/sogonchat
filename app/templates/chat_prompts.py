from typing import List

THERAPIST_SYSTEM_PROMPT = """당신은 전문 심리 상담사입니다. 다음 지침을 따라주세요:
1. 항상 공감적이고 지지적인 태도를 유지하세요
2. 판단하지 말고 경청하는 자세를 보여주세요
3. 필요한 경우 적절한 질문을 통해 내담자의 생각을 더 깊이 탐색하도록 도와주세요
4. 내담자의 감정을 인정하고 정당화해주세요"""

CHAT_TEMPLATE = """
관련된 이전 상담 내용:
{context}

대화 기록:
{chat_history}

내담자: {user_message}
상담사:"""

EMOTIONAL_KEYWORDS = [
    '슬프', '우울', '힘들', '행복', '기쁘', '화나', '불안',
    '걱정', '외롭', '답답', '스트레스', '희망', '절망'
]

def should_suggest_diary(messages: List[str], min_messages: int = 5) -> bool:
    if len(messages) < min_messages:
        return False
    
    recent_messages = messages[-3:]
    return any(
        keyword in message 
        for message in recent_messages 
        for keyword in EMOTIONAL_KEYWORDS
    ) 