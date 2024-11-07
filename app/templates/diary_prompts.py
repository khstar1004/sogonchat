DIARY_SYSTEM_PROMPT = """일기 작성을 위한 가이드라인:
1. 감정과 생각을 구체적으로 표현하세요
2. 자기 성찰적인 내용을 포함하세요
3. 긍정적인 관점이나 희망적인 메시지를 담아주세요
4. 일기는 1인칭 시점으로 작성해주세요"""

DIARY_TEMPLATE = """
대화 내용:
{chat_history}

다음 형식으로 작성해주세요:
감정 상태: [주요 감정을 한 단어로]

일기 내용:
[자세한 일기 내용]"""

def parse_diary_response(response: str) -> tuple[str, str]:
    """일기 응답을 감정과 내용으로 파싱"""
    parts = response.split('\n', 1)
    mood = parts[0].split(': ')[1].strip()
    content = parts[1].strip()
    return mood, content 