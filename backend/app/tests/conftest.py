from typing import Dict

import pytest

from app.adapters.repositories.expense import (
    AbstractExpenseRepository, FakeExpenseRepository
)
from app.domain.expense import Expense, ExpenseCreate


@pytest.fixture
def expense_create_payload() -> Dict:
    return {
        'name': 'fake expense',
        'value': 2.0,
        'description': 'fake description'
    }


@pytest.fixture
def expense_entity() -> Expense:
    return Expense(
        id=1,
        name='fake expense',
        value=2.0,
        description='fake description'
    )


@pytest.fixture
def expense_create_entity() -> ExpenseCreate:
    return ExpenseCreate(
        name='fake expense',
        value=2.0,
        description='fake description'
    )


@pytest.fixture
def fake_repository() -> AbstractExpenseRepository:
    return FakeExpenseRepository()
