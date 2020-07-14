import pytest
import mock

from entities.expenses import Expense


@pytest.fixture
def expense_entity():
    return Expense(
        name='fake expense',
        value=2.0,
        description='fake description'
    )


@pytest.fixture
def mock_repository() -> mock.MagicMock:
    return mock.MagicMock()
