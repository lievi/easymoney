from app.domain.expense import Expense, ExpenseCreation 
from app.repositories.expense import ExpensesRepository

from .exceptions import ExpenseNotFound


def create_expense(
    repository: ExpensesRepository, expense: ExpenseCreation 
) -> Expense:
    return repository.create(expense)


def get_by_id(
    repository: ExpensesRepository, expense_id: int
) -> Expense:
    expense = repository.get(expense_id)
    if not expense:
        raise ExpenseNotFound
    return expense
