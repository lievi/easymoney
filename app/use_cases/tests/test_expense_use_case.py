import pytest
import mock

from use_cases.expenses_use_case import CreateExpense
from interfaces.repositories.exceptions import (
    RepositoryException,
    RepositoryTimeoutException,
)


class TestCreateExpenseUseCase:
    def test_create_expense_should_save_expense_and_return_it_with_an_id(
        self, expense_entity, fake_repository
    ):
        use_case = CreateExpense(fake_repository)
        saved_entity = use_case.execute(expense_entity)

        assert saved_entity.id == fake_repository.PAYLOAD["id"]

    @pytest.mark.parametrize(
        "repo_exception", [RepositoryException, RepositoryTimeoutException]
    )
    def test_error_on_repository_when_saving_the_expense_should_raise(
        self, expense_entity, fake_repository, repo_exception
    ):
        with mock.patch.object(
            fake_repository, "create_expense", side_effect=repo_exception
        ):
            with pytest.raises(repo_exception):
                use_case = CreateExpense(fake_repository)
                use_case.execute(expense_entity)
