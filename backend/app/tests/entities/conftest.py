import pytest

from app.domain.expense import Expense


@pytest.fixture
def expense_payload() -> dict:
    return {
        'id': 1,
        'name': 'fake expense',
        'value': 2.0,
        'description': 'fake description'
    }


@pytest.fixture
def expense_entity(expense_payload: dict) -> Expense:
    return Expense(**expense_payload)
