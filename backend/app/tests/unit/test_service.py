# import pytest
from unittest.mock import patch

from app.domain.expense import Expense, ExpenseCreate
from app.services.expense import create_expense, get_by_id
from app.services.unit_of_work import AbstractUnitOfWork


class TestExpenseService:
    def test_create_expense_should_persist_expense_and_return_it(
        self,
        expense_create_entity: ExpenseCreate,
        fake_uow: AbstractUnitOfWork,
    ) -> None:
        with patch.object(fake_uow, 'commit') as mock_commit:
            new_entity = create_expense(fake_uow, expense_create_entity)
            assert mock_commit.called

        assert new_entity.name == expense_create_entity.name
        assert new_entity.value == expense_create_entity.value
        assert new_entity.description == expense_create_entity.description

    def test_get_expense_by_id(
        self,
        expense_entity: Expense,
        fake_uow: AbstractUnitOfWork
    ) -> None:
        fake_uow.expenses._expenses.append(expense_entity)
        entity = get_by_id(fake_uow, expense_entity.id)

        assert entity == expense_entity
