from app.entities.expenses import Expense
from app.use_cases.abstract_use_case import AbstractUseCase

from app.interfaces.repositories.expense_repository import (
    AbstractExpenseRepository,
)


class CreateExpense(AbstractUseCase):
    """ Creates an expense to a certain user """
    def __init__(self, repository: AbstractExpenseRepository) -> None:
        self.repository = repository

    def execute(self, expense: Expense) -> Expense:
        expense = self.repository.create_expense(expense)
        return expense


class GetExpenseById(AbstractUseCase):
    """ Get an Expense by id """
    def __init__(self, repository: AbstractExpenseRepository) -> None:
        self.repository = repository

    def execute(self, expense_id: int) -> Expense:
        return self.repository.get_expense_by_id(expense_id)
