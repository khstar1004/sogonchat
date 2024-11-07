therapy_chatbot/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── config/
│   │   ├── __init__.py
│   │   └── settings.py
│   ├── core/
│   │   ├── __init__.py
│   │   ├── database.py
│   │   └── logger.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── chat.py
│   │   └── diary.py
│   ├── routers/
│   │   ├── __init__.py
│   │   ├── chat_routes.py
│   │   └── diary_routes.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── chat_service.py
│   │   ├── diary_service.py
│   │   └── rag_service.py
│   ├── templates/
│   │   ├── __init__.py
│   │   ├── chat_prompts.py
│   │   └── diary_prompts.py
│   └── data/
│       └── chat_diary_dataset.json
├── .env
├── requirements.txt
└── README.md