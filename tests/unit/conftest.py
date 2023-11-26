import pytest

from app.repositories.expense import FakeExpenseRepository


@pytest.fixture
def fake_repository():
    return FakeExpenseRepository()
