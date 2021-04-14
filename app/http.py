from fastapi import FastAPI
from app.routes import router

api = FastAPI()
api.include_router(router)
