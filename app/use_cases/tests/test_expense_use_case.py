import pytest
import mock

from use_cases.expenses_use_case import CreateExpense


class TestCreateExpenseUseCase:
    def test_create_expense_should_save_new_expense_and_return_it(
        self, expense_entity, mock_repository
    ):
        use_case = CreateExpense(mock_repository)
        saved_entity = use_case.execute(expense_entity)
        assert mock_repository.called_with('groselha')
        assert saved_entity == expense_entity
