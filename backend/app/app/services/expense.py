from app.domain.expense import Expense, ExpenseCreate
from app.adapters.repositories.expense import AbstractExpenseRepository


def create_expense(
    repository: AbstractExpenseRepository, expense: ExpenseCreate
) -> Expense:
    expense = repository.create(expense)
    return expense


def get_by_id(
    repository: AbstractExpenseRepository, expense_id: int
) -> Expense:
    return repository.get(expense_id)
