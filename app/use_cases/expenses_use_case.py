from typing import Dict, Optional
from entities.expenses import Expense

from interfaces.repositories.expense_repository import (
    AbstractExpenseRepository,
)
from interfaces.use_cases.expense_use_case import AbstractExpenseUseCase


class CreateExpense(AbstractExpenseUseCase):
    """ Creates an expense to a certain user """
    def __init__(self, repository: AbstractExpenseRepository) -> None:
        self.repository = repository

    def execute(self, expense: Expense) -> Expense:
        saved_expense = self.repository.create_expense(expense)
        return saved_expense


class GetExpenseById(AbstractExpenseUseCase):
    """ Get an Expense by id """
    def __init__(self, repository: AbstractExpenseRepository) -> None:
        self.repository = repository

    def execute(self, expense_id: int) -> Expense:
        return self.repository.get_expense_by_id(expense_id)
