from pydantic import BaseModel


class BaseExpense(BaseModel):
    name: str
    description: str | None
    value: float


class Expense(BaseExpense):
    id: int


class ExpenseCreation(BaseExpense):
    pass
