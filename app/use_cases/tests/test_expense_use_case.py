import pytest
import mock

from use_cases.expenses_use_case import CreateExpense


class TestCreateExpenseUseCase:
    def test_create_expense_should_save_expense_and_return_it_with_an_id(
        self, expense_entity, mock_repository
    ):
        id = 'some-id'
        mock_repository.create_expense.return_value = id

        use_case = CreateExpense(mock_repository)
        saved_entity = use_case.execute(expense_entity)

        assert mock_repository.create_expense.called
        assert saved_entity.id == id

    def test_error_on_repository_when_saving_the_expense_should_raise(
        self
    ):
        pass
