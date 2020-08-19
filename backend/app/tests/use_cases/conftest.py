from typing import Dict

import pytest

from app.entities.expenses import Expense
from app.infrastructure.repositories.expense.fake_expense_repository import (
    FakeExpenseRepository
)


@pytest.fixture
def expense_payload() -> Dict:
    return {
        'name': 'fake expense',
        'value': 2.0,
        'description': 'fake description'
    }


@pytest.fixture
def expense_entity() -> Expense:
    return Expense(
        name='fake expense',
        value=2.0,
        description='fake description'
    )


@pytest.fixture
def fake_repository() -> FakeExpenseRepository:
    return FakeExpenseRepository()
