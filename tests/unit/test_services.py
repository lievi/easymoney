from unittest.mock import patch
import pytest

from app.domain.expense import ExpenseCreate
from app.services.exceptions import ExpenseNotFound
from app.services.expenses import create_expense, get_by_id
from app.services.unit_of_work import FakeUnitOfWork


class TestExpenseService:
    def test_create_expense_should_persist_expense_and_return_it(
        self,
        expense_create_entity: ExpenseCreate,
        fake_uow: FakeUnitOfWork,
    ) -> None:
        create_expense(fake_uow, expense_create_entity)

        assert fake_uow.expenses._expenses is not None

        expense = fake_uow.expenses._expenses[-1]

        assert expense.name == expense_create_entity.name
        assert expense.description == expense_create_entity.description
        assert expense.value == expense_create_entity.value

    def test_get_expense_by_id(
        self,
        expense_create_entity: ExpenseCreate,
        fake_uow: FakeUnitOfWork
    ) -> None:
        create_expense(fake_uow, expense_create_entity)
        expense_id = fake_uow.expenses._expenses[-1].id

        expense = get_by_id(fake_uow, expense_id)

        assert expense.name == expense_create_entity.name
        assert expense.description == expense_create_entity.description
        assert expense.value == expense_create_entity.value

    def test_get_expense_with_nonexistent_id_should_raise_exception(
        self,
        fake_uow: FakeUnitOfWork
    ) -> None:
        with pytest.raises(ExpenseNotFound):
            get_by_id(fake_uow, 999)
