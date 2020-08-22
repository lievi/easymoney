from app.entities.expenses import Expense

from app.interfaces.repositories.expense_repository import (
    AbstractExpenseRepository,
)
from app.interfaces.use_cases.expense_use_case import AbstractExpenseUseCase


class CreateExpense(AbstractExpenseUseCase):
    """ Creates an expense to a certain user """
    def __init__(self, repository: AbstractExpenseRepository) -> None:
        self.repository = repository

    def execute(self, expense: Expense) -> Expense:
        expense_id = self.repository.create_expense(expense)

        # Adding the id of the saved expense on the entity
        expense.id = expense_id
        return expense


class GetExpenseById(AbstractExpenseUseCase):
    """ Get an Expense by id """
    def __init__(self, repository: AbstractExpenseRepository) -> None:
        self.repository = repository

    def execute(self, expense_id: int) -> Expense:
        return self.repository.get_expense_by_id(expense_id)
