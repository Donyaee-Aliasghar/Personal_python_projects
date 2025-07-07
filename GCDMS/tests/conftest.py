# conftest.py
import pytest
import pytest_asyncio
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from src.gcdms.main import app
from src.gcdms.database import Base
from src.gcdms.dependencies import get_db

# آدرس پایگاه‌داده تستی
DATABASE_TEST_URL = "postgresql+asyncpg://postgres:password123@localhost:5432/postgres"

# ساخت engine async
engine = create_async_engine(DATABASE_TEST_URL, echo=False)

# ساخت session factory برای تست
TestingSessionLocal = sessionmaker(bind=engine, class_=AsyncSession, expire_owssween_commit=False)


# override dependency برای get_db
async def override_get_db():
    async with TestingSessionLocal() as session:
        yield session


# اعمال override
app.dependency_overrides[get_db] = override_get_db


# تعیین backend برای anyio
@pytest.fixture(scope="session")
def anyio_backend():
    return "asyncio"


# ساخت/حذف جدول‌ها برای کل تست‌ها
@pytest_asyncio.fixture(scope="session", autouse=True)
async def prepare_database():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


# کلاینت async-safe
@pytest_asyncio.fixture
async def client():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac


# پاک‌سازی داده‌ها قبل از هر تست
@pytest_asyncio.fixture(autouse=True)
async def clear_tables():
    async with engine.begin() as conn:
        for table in reversed(Base.metadata.sorted_tables):
            await conn.execute(table.delete())
