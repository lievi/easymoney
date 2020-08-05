from app.entities.expenses import Expense
from app.infrastructure.api.resources.expenses.schemas import (
    ExpenseSchema,
    ExpenseOutputSchema
)


class ExpenseAdapter:
    @staticmethod
    def from_entity(expense: ExpenseOutputSchema) -> ExpenseSchema:
        return ExpenseOutputSchema.from_orm(expense)

    @staticmethod
    def to_entity(expense_create: ExpenseSchema) -> ExpenseOutputSchema:
        return Expense.from_dict(expense_create.dict())
