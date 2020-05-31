from entities.expenses import Expense
from interfaces.repositories.expense_repository import (
    AbstractExpenseRepository,
)
from interfaces.use_case import AbstractUseCase


class CreateExpense(AbstractUseCase):
    """ Creates an expense to a certain user """

    def __init__(self, repository: AbstractExpenseRepository):
        self.repository = repository

    def execute(self, expense: Expense, user) -> None:
        # Put some business logic here
        self.repository.create(expense)
