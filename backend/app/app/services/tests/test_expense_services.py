# import pytest
# import mock

from app.adapters.repositories.expense import FakeExpenseRepository
from app.domain.expense import Expense, ExpenseCreate
from app.services.expense import create_expense, get_by_id


class TestCreateExpense:
    def test_create_expense_should_persist_expense_and_return_it(
        self,
        expense_create_entity: ExpenseCreate
    ) -> None:
        fake_repo = FakeExpenseRepository()
        new_entity = create_expense(fake_repo, expense_create_entity)

        assert new_entity == expense_create_entity

    def test_get_expense_by_id(
        self,
        expense_entity: Expense
    ) -> None:
        fake_repo = FakeExpenseRepository([expense_entity])
        new_entity = get_by_id(fake_repo, expense_entity.id)

        assert new_entity == expense_entity
