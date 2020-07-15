from entities.expenses import Expense
from .schemas import (
    ExpenseSchema,
    ExpenseOutputSchema
)


class ExpenseAdapter:
    @staticmethod
    def from_entity(expense: ExpenseOutputSchema):
        return ExpenseOutputSchema.from_orm(expense)

    @staticmethod
    def to_entity(expense_create: ExpenseSchema):
        return Expense.from_dict(expense_create.dict())
