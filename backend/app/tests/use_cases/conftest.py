from typing import Dict

import pytest

from app.adapters.expense.fake_expense_repository import (
    FakeExpenseRepositoryAdapter
)
from app.domain.expense import Expense


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
def fake_repository() -> FakeExpenseRepositoryAdapter:
    return FakeExpenseRepositoryAdapter()
