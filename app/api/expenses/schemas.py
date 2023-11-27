from app.domain.expense import Expense, ExpenseCreation


class BaseExpenseSchema(Expense):
    pass


class ExpenseSchema(BaseExpenseSchema):
    pass


class CreateExpenseSchema(ExpenseCreation):
    class Config:
        from_orm = True
