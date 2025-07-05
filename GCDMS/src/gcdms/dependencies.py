# Defining Dependency to get Database Session

from typing import AsyncGenerator
from .database import async_session


async def get_db() -> AsyncGenerator:
    async with async_session() as session:
        yield session
