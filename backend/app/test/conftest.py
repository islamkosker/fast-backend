import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from app.main import app
from app.core.config import settings

# Veritabanı engine (sync, çünkü SQLAlchemy sync)
@pytest.fixture(scope="session")
def engine():
    return create_engine(str(settings.SQLALCHEMY_DATABASE_URI))

# Sync session (şimdilik async'e gerek yok)
@pytest.fixture(scope="function")
def db_session(engine):
    TestingSessionLocal = scoped_session(
        sessionmaker(autocommit=False, autoflush=False, bind=engine)
    )
    session = TestingSessionLocal()
    try:
        yield session
    finally:
        session.close()
        TestingSessionLocal.remove()


@pytest.fixture(scope="function")
def client():
    with TestClient(app) as c:
        yield c

# --- Import and Register Factory Fixtures ---

from app.test.fixtures.factory import (
    user_factory,
    device_factory,
)

# --- Composite Test Data Fixtures ---

from app.test.fixtures.fixtures import (
    mock_multiple_users,
    mock_user_with_devices,
)