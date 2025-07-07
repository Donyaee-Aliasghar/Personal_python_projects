# Defining Dependency to get Database Session

from .database import async_session
from contextlib import asynccontextmanager


@asynccontextmanager
async def get_db():
    async with async_session() as session:
        yield session
