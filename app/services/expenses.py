
from app.domain.expense import Expense, ExpenseCreation, ExpenseUpdate

from app.repositories.expense import ExpensesRepository

from .exceptions import ExpenseNotFound


def create_expense(
    repository: ExpensesRepository, expense: ExpenseCreation
) -> Expense:
    return repository.create(expense)


def get_by_id(repository: ExpensesRepository, expense_id: int) -> Expense:
    expense = repository.get(expense_id)
    if not expense:
        raise ExpenseNotFound
    return expense


def update_expense(
    repository: ExpensesRepository,
    expense_id: int,
    update_model: ExpenseUpdate,
) -> Expense:
    updated_expense = repository.update(expense_id, update_model)

    if not updated_expense:
        raise ExpenseNotFound
    return updated_expense

