from fastapi import FastAPI
from contextlib import asynccontextmanager

from app.database import engine
from app.modules import Base
from app.routers import notes

@asynccontextmanager
async def lifespan(_app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

        yield

app = FastAPI(lifespan=lifespan)

app.include_router(notes.router, prefix="/notes")