import pytest

from app.entities.expenses import Expense


class TestExpenseEntity:
    def test_create_expense_should_return_expense(
        self, expense_payload: dict
    ) -> None:
        new_expense = Expense(
            name=expense_payload['name'],
            value=expense_payload['value'],
            description=expense_payload['description'],
        )

        assert isinstance(new_expense, Expense)
        assert new_expense.to_dict() == expense_payload

    def test_create_expense_without_optional_attr_should_return_expense(
        self, expense_payload: dict
    ) -> None:
        new_expense = Expense(
            name=expense_payload['name'], value=expense_payload['value'],
        )

        assert isinstance(new_expense, Expense)
        assert new_expense.name == expense_payload['name']
        assert new_expense.value == expense_payload['value']

    def test_create_expense_without_required_attr_should_raise_exception(
        self, expense_payload: dict
    ) -> None:
        with pytest.raises(TypeError):
            Expense(name=expense_payload['name'])

    def test_create_expense_from_dict_shoud_return_expense(
        self, expense_payload: dict
    ) -> None:
        new_expense = Expense.from_dict(expense_payload)

        assert isinstance(new_expense, Expense)
        assert new_expense.name == expense_payload['name']
        assert new_expense.value == expense_payload['value']
        assert new_expense.description == expense_payload['description']

    def test_expense_to_dict_shoud_return_dict(
        self, expense_entity: Expense
    ) -> None:
        expense_dict = expense_entity.to_dict()

        assert isinstance(expense_dict, dict)
        assert expense_entity.name == expense_dict['name']
        assert expense_entity.value == expense_dict['value']
        assert expense_entity.description == expense_dict['description']
