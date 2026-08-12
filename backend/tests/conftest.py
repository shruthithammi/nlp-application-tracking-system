import os
os.environ["DATABASE_URL"] = "sqlite:///./test_clearhire.db"
os.environ["SECRET_KEY"] = "test-secret"
from fastapi.testclient import TestClient
import pytest
from app.main import app
from app.database.connection import Base, engine
@pytest.fixture(autouse=True)
def reset_db():
    Base.metadata.drop_all(bind=engine); Base.metadata.create_all(bind=engine); yield
@pytest.fixture
def client():
    with TestClient(app) as c: yield c
