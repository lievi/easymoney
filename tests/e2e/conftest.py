from typing import Generator

import pytest
from fastapi.testclient import TestClient

from easymoney.api.dependencies import get_session
from easymoney.main import app
from easymoney.repositories.expense import SqlModelExpenseRepository
from easymoney.verify_dependencies import verify_dependencies


@pytest.fixture
def client() -> Generator:
    with TestClient(app) as client:
        yield client


@pytest.fixture(scope="session")
def wait_dependencies() -> None:
    verify_dependencies()


@pytest.fixture
def db_session():
    return next(get_session())


# TODO: how to get this repo dynamically, or use bare sql
@pytest.fixture
def expense_repository(db_session):
    return SqlModelExpenseRepository(session=db_session)
