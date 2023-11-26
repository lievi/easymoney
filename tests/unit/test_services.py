import pytest

from app.services.exceptions import ExpenseNotFound
from app.services.expenses import create_expense, get_by_id
from app.domain.expense import ExpenseCreation
from app.repositories.expense import FakeExpenseRepository


class TestExpenseService:
    def test_create_expense_should_persist_expense_and_return_it(
        self,
        expense_create_entity: ExpenseCreation,
        fake_repository: FakeExpenseRepository,
    ) -> None:
        create_expense(fake_repository, expense_create_entity)

        assert fake_repository._expenses is not None

        expense = fake_repository._expenses[-1]

        assert expense.name == expense_create_entity.name
        assert expense.description == expense_create_entity.description
        assert expense.value == expense_create_entity.value

    def test_get_expense_by_id(
        self,
        expense_create_entity: ExpenseCreation,
        fake_repository: FakeExpenseRepository,
    ) -> None:
        create_expense(fake_repository, expense_create_entity)
        expense_id = fake_repository._expenses[-1].id

        expense = get_by_id(fake_repository, expense_id)

        assert expense.name == expense_create_entity.name
        assert expense.description == expense_create_entity.description
        assert expense.value == expense_create_entity.value

    def test_get_expense_with_nonexistent_id_should_raise_exception(
        self, fake_repository: FakeExpenseRepository
    ) -> None:
        with pytest.raises(ExpenseNotFound):
            get_by_id(fake_repository, 999)
