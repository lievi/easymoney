from typing import Generator

import pytest
from fastapi.testclient import TestClient

from app.services.unit_of_work import SqlAlchemyUnitOfWork
from app.main import app

from app.db.session import engine
from app.verify_dependencies import verify_dependencies


@pytest.fixture
def client() -> Generator:
    with TestClient(app) as client:
        yield client


@pytest.fixture
def uow() -> SqlAlchemyUnitOfWork:
    return SqlAlchemyUnitOfWork()

@pytest.fixture(scope="session")
def wait_dependencies() -> None:
    verify_dependencies()
