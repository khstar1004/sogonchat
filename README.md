# Therapy Chatbot API

심리 상담 챗봇 API 서버입니다. OpenAI의 GPT 모델을 활용하여 사용자와 대화하고, 감정 상태를 분석하여 일기 작성을 제안합니다.

## 주요 기능

1. 심리 상담 대화
   - 공감적이고 지지적인 대화 제공
   - 이전 대화 컨텍스트 활용
   - 감정 키워드 기반 일기 작성 제안

2. AI 일기 생성
   - 대화 내용 기반 일기 자동 생성
   - 감정 상태 분석 및 기록
   - 자기 성찰적 내용 포함

3. 대화 및 일기 히스토리 관리
   - 사용자별 대화 기록 저장
   - 생성된 일기 저장 및 조회

## 기술 스택

- FastAPI
- LangChain
- OpenAI GPT
- Supabase
- FAISS (벡터 검색)

## 설치 방법

1. 저장소 클론 
bash
git clone [repository-url]
cd therapy-chatbot


2. 가상환경 생성 및 활성화
bash
python -m venv venv
source venv/bin/activate # Windows: venv\Scripts\activate



3. 의존성 설치
bash
pip install -r requirements.txt


4. 환경 변수 설정
`.env` 파일을 생성하고 다음 내용을 입력:

API Configuration
API_V1_STR=/api
PROJECT_NAME="Therapy Chatbot API"
OpenAI Configuration
OPENAI_API_KEY=your_openai_api_key
MODEL_NAME=gpt-4o-mini
Chat Configuration
CHAT_HISTORY_LENGTH=5
Data Configuration
DATA_PATH=app/data/chat_diary_dataset.json
Supabase Configuration
SUPABASE_URL=your_supabase_project_url
SUPABASE_KEY=your_supabase_anon_key


## 실행 방법

개발 서버 실행:
bash
uvicorn app.main:app --reload



## API 엔드포인트

### 채팅 API
- POST `/api/chat/message`
  - 새로운 메시지 전송 및 응답 받기
  - Request Body: `ChatHistory` (메시지 목록 및 사용자 ID)
  - Response: `ChatResponse` (봇 응답 및 일기 작성 제안)

### 일기 API
- POST `/api/diary/generate`
  - 대화 내용 기반 일기 생성
  - Request Body: `ChatHistory` (메시지 목록 및 사용자 ID)
  - Response: `ChatResponse` (봇 응답 및 일기 작성 제안)

## 배포 방법

1. Docker 이미지 빌드
bash
docker build -t therapy-chatbot .


2. Docker 컨테이너 실행
bash
docker run -d -p 8000:8000 therapy-chatbot



## Supabase 데이터베이스 설정

1. 필요한 테이블:
   - chat_messages
     - user_id (text)
     - role (text)
     - content (text)
     - timestamp (timestamptz)
   
   - diaries
     - user_id (text)
     - content (text)
     - mood (text)
     - timestamp (timestamptz)

2. 테이블 생성 SQL:

sql
-- 채팅 메시지 테이블
CREATE TABLE chat_messages (
id SERIAL PRIMARY KEY,
user_id TEXT NOT NULL,
role TEXT NOT NULL,
content TEXT NOT NULL,
timestamp TIMESTAMPTZ DEFAULT NOW()
);
-- 일기 테이블
CREATE TABLE diaries (
id SERIAL PRIMARY KEY,
user_id TEXT NOT NULL,
content TEXT NOT NULL,
mood TEXT NOT NULL,
timestamp TIMESTAMPTZ DEFAULT NOW()
);


## API 문서

서버 실행 후 다음 URL에서 API 문서 확인 가능:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## 라이선스

MIT License