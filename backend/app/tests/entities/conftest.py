import pytest

from app.entities.expenses import Expense


@pytest.fixture
def expense_payload() -> dict:
    return {
        'name': 'fake expense',
        'value': 2.0,
        'description': 'fake description'
    }


@pytest.fixture
def expense_entity(expense_payload: dict) -> Expense:
    return Expense.from_dict(expense_payload)
