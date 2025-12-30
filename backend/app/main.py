from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import chat
from contextlib import asynccontextmanager
from app.core.db import engine
from sqlmodel import SQLModel

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Create tables on startup (for simple dev setups)
    # In prod, use Alembic
    SQLModel.metadata.create_all(engine)
    yield

app = FastAPI(title="AI Todo Chatbot", lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chat.router, prefix="/api")

@app.get("/")
def read_root():
    return {"message": "Welcome to AI Todo Chatbot API"}
