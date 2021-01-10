# import pytest
# import mock

from app.adapters.repositories.expense import (
    AbstractExpenseRepository,
    FakeExpenseRepository,
)
from app.domain.expense import Expense, ExpenseCreate
from app.services.expense import create_expense, get_by_id


class TestExpenseService:
    def test_create_expense_should_persist_expense_and_return_it(
        self,
        expense_create_entity: ExpenseCreate,
        fake_repository: AbstractExpenseRepository,
    ) -> None:
        new_entity = create_expense(fake_repository, expense_create_entity)

        assert new_entity.name == expense_create_entity.name
        assert new_entity.value == expense_create_entity.value
        assert new_entity.description == expense_create_entity.description

    def test_get_expense_by_id(
        self,
        expense_entity: Expense,
        fake_repository: FakeExpenseRepository,
    ) -> None:
        fake_repository._expenses.append(expense_entity)
        entity = get_by_id(fake_repository, expense_entity.id)

        assert entity == expense_entity
