from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="Documentation Agent")

app.include_router(router)