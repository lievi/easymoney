import pytest

from easymoney.repositories.expense import FakeExpenseRepository


@pytest.fixture
def fake_repository():
    return FakeExpenseRepository()
