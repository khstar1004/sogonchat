# Therapy Chatbot API

심리 상담 챗봇 API 서버 - OpenAI GPT 기반의 대화형 심리 상담 및 AI 일기 생성 서비스

## 💡 주요 기능

### 1. 심리 상담 대화
- 공감적이고 지지적인 대화 제공
- 이전 대화 컨텍스트 활용
- 감정 키워드 기반 일기 작성 제안

### 2. AI 일기 생성
- 대화 내용 기반 일기 자동 생성
- 감정 상태 분석 및 기록
- 자기 성찰적 내용 포함

### 3. 대화 및 일기 히스토리 관리
- 사용자별 대화 기록 저장
- 생성된 일기 저장 및 조회

## 🛠 기술 스택

- **Backend**: FastAPI
- **AI/ML**: LangChain, OpenAI GPT
- **Database**: Supabase
- **Vector Search**: FAISS

## 🚀 시작하기

### 설치 방법

1. **저장소 클론**
```bash
git clone [repository-url]
cd therapy-chatbot
```

2. **가상환경 설정**
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

3. **의존성 설치**
```bash
pip install -r requirements.txt
```

### 환경 변수 설정

`.env` 파일을 생성하고 다음 내용을 입력:

```plaintext
# API Configuration
API_V1_STR=/api
PROJECT_NAME="Therapy Chatbot API"

# OpenAI Configuration
OPENAI_API_KEY=your_openai_api_key
MODEL_NAME=gpt-4-mini

# Chat Configuration
CHAT_HISTORY_LENGTH=5

# Data Configuration
DATA_PATH=app/data/chat_diary_dataset.json

# Supabase Configuration
SUPABASE_URL=your_supabase_project_url
SUPABASE_KEY=your_supabase_anon_key
```

### 실행 방법

```bash
uvicorn app.main:app --reload
```

## 📌 API 엔드포인트

### 채팅 API
- **POST** `/api/chat/message`
  - 새로운 메시지 전송 및 응답 받기
  - Request Body: `ChatHistory`
  - Response: `ChatResponse`

### 일기 API
- **POST** `/api/diary/generate`
  - 대화 내용 기반 일기 생성
  - Request Body: `ChatHistory`
  - Response: `DiaryResponse`

## 🐳 Docker 배포

```bash
# 이미지 빌드
docker build -t therapy-chatbot .

# 컨테이너 실행
docker run -d -p 8000:8000 therapy-chatbot
```

## 📊 데이터베이스 설정

### Supabase 테이블 구조

1. **chat_messages 테이블**
```sql
CREATE TABLE chat_messages (
    id SERIAL PRIMARY KEY,
    user_id TEXT NOT NULL,
    role TEXT NOT NULL,
    content TEXT NOT NULL,
    timestamp TIMESTAMPTZ DEFAULT NOW()
);
```

2. **diaries 테이블**
```sql
CREATE TABLE diaries (
    id SERIAL PRIMARY KEY,
    user_id TEXT NOT NULL,
    content TEXT NOT NULL,
    mood TEXT NOT NULL,
    timestamp TIMESTAMPTZ DEFAULT NOW()
);
```

## 📚 API 문서

서버 실행 후 다음 URL에서 API 문서 확인 가능:
- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

## 📝 라이선스

MIT License

---

© 2024 Therapy Chatbot API. All rights reserved.
