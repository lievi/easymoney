import pytest

from app.repositories.expense import (
    ExpensesRepository, FakeExpenseRepository
)
from app.domain.expense import Expense
from app.api.expenses.schemas import CreateExpenseSchema


@pytest.fixture
def expense_create_payload() -> dict:
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
def expense_create_entity() -> CreateExpenseSchema:
    return CreateExpenseSchema(
        name='fake expense',
        value=2.0,
        description='fake description'
    )
