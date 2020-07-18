from fastapi.encoders import jsonable_encoder

from entities.expenses import Expense
from infrastructure.db.models.expense import Expense as ExpenseModel


class ExpenseDBAdapter:
    @staticmethod
    def from_entity(expense: Expense) -> ExpenseModel:
        json_expense = jsonable_encoder(expense)
        return ExpenseModel(**json_expense)

    @staticmethod
    def to_entity(expense: ExpenseModel) -> Expense:
        expense_entity = Expense(
            name=expense.name,
            value=expense.value,
            description=expense.description
        )
        expense_entity.id = expense.id
        return expense_entity
