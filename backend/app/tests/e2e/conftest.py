from typing import Generator

import pytest
from fastapi.testclient import TestClient

from app.services.unit_of_work import SqlAlchemyUnitOfWork
from app.main import app


@pytest.fixture
def client() -> Generator:
    with TestClient(app) as client:
        yield client


@pytest.fixture
def uow() -> SqlAlchemyUnitOfWork:
    return SqlAlchemyUnitOfWork()
