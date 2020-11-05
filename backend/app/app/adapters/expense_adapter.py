from fastapi.encoders import jsonable_encoder

from app.entities.expenses import Expense, ExpenseCreate
from app.infrastructure.db.models.expense import Expense as ExpenseModel


class ExpenseDBAdapter:
    @staticmethod
    def from_entity(expense_entity: ExpenseCreate) -> ExpenseModel:
        json_expense = jsonable_encoder(expense_entity)
        return ExpenseModel(**json_expense)

    @staticmethod
    def to_entity(expense_model: ExpenseModel) -> Expense:
        expense_entity = Expense(
            id=expense_model.id,
            name=expense_model.name,
            value=expense_model.value,
            description=expense_model.description
        )
        return expense_entity


expense_adapter = ExpenseDBAdapter()
