import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.gcdms.main import app
from src.gcdms.database import Base
from src.gcdms.dependencies import get_db

# shared in-memory SQLite
SQLALCHEMY_DATABASE_URL = "sqlite:///file::memory:?cache=shared"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False, "uri": True},
)
TestingSessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)


@pytest.fixture(scope="session", autouse=True)
def prepare_database():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)


def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db


@pytest.fixture(scope="module")
def client():
    with TestClient(app) as c:
        yield c


@pytest.fixture(autouse=True)
def clear_tables():
    yield
    from src.gcdms.database import Base
    from src.gcdms.dependencies import get_db

    db = next(override_get_db())
    for table in reversed(Base.metadata.sorted_tables):
        db.execute(table.delete())
    db.commit()
