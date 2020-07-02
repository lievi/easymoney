from typing import Optional
from entities.expenses import Expense

from interfaces.repositories.expense_repository import (
    AbstractExpenseRepository,
)
from interfaces.use_cases.expense_use_case import AbstractExpenseUseCase


class CreateExpense(AbstractExpenseUseCase):
    """ Creates an expense to a certain user """
    def __init__(self, repository: AbstractExpenseRepository) -> None:
        self.repository = repository

    def execute(self, expense: Expense) -> None:
        # Put some business logic here
        self.repository.create_expense(expense)


class GetExpenseById(AbstractExpenseUseCase):
    """ Get an Expense by id """
    def __init__(self, repository: AbstractExpenseRepository) -> None:
        self.repository = repository

    def execute(self, expense_id: int) -> Expense:
        return self.repository.get_expense_by_id(expense_id)
