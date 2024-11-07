from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware

from app.routers import chat_routes

from app.config.settings import settings

from app.core.logger import logger



app = FastAPI(

    title=settings.PROJECT_NAME,

    openapi_url=f"{settings.API_V1_STR}/openapi.json"

)



# CORS 미들웨어 설정

app.add_middleware(

    CORSMiddleware,

    allow_origins=["*"],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"],

)



# 라우터 등록

app.include_router(

    chat_routes.router,

    prefix=f"{settings.API_V1_STR}/chat",

    tags=["chat"]

)



@app.on_event("startup")

async def startup_event():

    logger.info("Starting up the application...")



@app.on_event("shutdown")

async def shutdown_event():

    logger.info("Shutting down the application...")














