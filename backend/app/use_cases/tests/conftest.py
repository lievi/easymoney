import pytest
import mock

from app.entities.expenses import Expense
from infrastructure.repositories.expense.fake_expense_repository import (
    FakeExpenseRepository
)


@pytest.fixture
def expense_payload():
    return {
        'name': 'fake expense',
        'value': 2.0,
        'description': 'fake description'
    }


@pytest.fixture
def expense_entity():
    return Expense(
        name='fake expense',
        value=2.0,
        description='fake description'
    )


@pytest.fixture
def fake_repository() -> FakeExpenseRepository:
    return FakeExpenseRepository()
