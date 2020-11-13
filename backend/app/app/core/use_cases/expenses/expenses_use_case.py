from app.core.entities.expense import Expense, ExpenseCreate
from app.core.use_cases.abstract_use_case import AbstractUseCase

from app.core.ports.expenses.expense_repository import (
    ExpenseRepository
)


class CreateExpense(AbstractUseCase):
    """ Creates an expense to a certain user """
    def __init__(self, repository: ExpenseRepository) -> None:
        self.repository = repository

    def execute(self, expense: ExpenseCreate) -> Expense:
        expense = self.repository.create(expense)
        return expense


class GetExpenseById(AbstractUseCase):
    """ Get an Expense by id """
    def __init__(self, repository: ExpenseRepository) -> None:
        self.repository = repository

    def execute(self, expense_id: int) -> Expense:
        return self.repository.get(expense_id)
