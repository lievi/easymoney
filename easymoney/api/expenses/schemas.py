from easymoney.domain.expense import Expense, ExpenseCreation, ExpenseFullUpdate


class BaseExpenseSchema(Expense):
    pass


class ExpenseSchema(BaseExpenseSchema):
    pass


class CreateExpenseSchema(ExpenseCreation):
    class Config:
        from_orm = True


class UpdateExpenseSchema(ExpenseFullUpdate):
    class Config:
        from_orm = True
