import pytest
import mock

from app.core.entities.expense import Expense
from app.core.use_cases.abstract_use_case import AbstractUseCase
from app.core.use_cases.expenses.expenses_use_case import (
    CreateExpense, GetExpenseById
)
from app.core.ports.expenses.expense_repository import ExpenseRepository
# from app.interfaces.repositories.exceptions import (
#     RepositoryException,
#     RepositoryTimeoutException,
# )


class TestCreateExpenseUseCase:
    @pytest.fixture
    def create_expense_use_case(
        self, fake_repository: ExpenseRepository
    ) -> AbstractUseCase:
        return CreateExpense(fake_repository)

    def test_create_expense_should_save_expense_and_return_it(
        self,
        expense_entity: Expense,
        fake_repository: ExpenseRepository,
    ) -> None:
        use_case = CreateExpense(fake_repository)
        saved_entity = use_case.execute(expense_entity)

        assert saved_entity == fake_repository.PAYLOAD

    # @pytest.mark.parametrize(
    #     "repo_exception", [RepositoryException, RepositoryTimeoutException]
    # )
    # def test_error_on_repository_when_saving_the_expense_should_raise_exception(  # noqa
    #     self,
    #     expense_entity: Expense,
    #     fake_repository: ExpenseRepository,
    #     repo_exception: RepositoryException,
    # ) -> None:
    #     with mock.patch.object(
    #         fake_repository, "create_expense", side_effect=repo_exception
    #     ):
    #         with pytest.raises(repo_exception):
    #             use_case = CreateExpense(fake_repository)
                # use_case.execute(expense_entity)


class TestGetExpenseById:
    @pytest.fixture
    def get_expense_by_id_use_case(
        self, fake_repository: ExpenseRepository
    ) -> GetExpenseById:
        return GetExpenseById(fake_repository)

    def test_get_expense_by_id_should_return_expense(
        self,
        get_expense_by_id_use_case: GetExpenseById,
        fake_repository: ExpenseRepository
    ) -> None:
        expense = get_expense_by_id_use_case.execute(
            fake_repository.PAYLOAD["id"]
        )
        assert expense.__dict__ == fake_repository.PAYLOAD

    def test_id_not_found_when_get_expense_by_id_should_raise_exception(
        self
    ) -> None:
        pass

    def test_repository_error_when_get_expense_by_id_should_raise_exception(
        self
    ) -> None:
        pass
