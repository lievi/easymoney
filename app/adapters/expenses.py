from entities.expenses import Expense
from infrastructure.db.models.expense import Expense as ExpenseDB


def db_model_to_entity(expense: ExpenseDB):
    return Expense(
        id=expense.id,
        name=expense.name,
        value=expense.value,
        description=expense.description
    )
