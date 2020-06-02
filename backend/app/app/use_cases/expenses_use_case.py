from typing import Optional
from entities.expenses import Expense

from interfaces.repositories.expense_repository import (
    AbstractExpenseRepository,
)
from interfaces.use_case import AbstractUseCase


class CreateExpense(AbstractUseCase):
    """ Creates an expense to a certain user """

    def __init__(self, repository: AbstractExpenseRepository):
        self.repository = repository

    def execute(
        self, name: str, value: float, description: Optional[str] = None
    ) -> None:
        new_expense = Expense(name=name, value=value, description=description)

        # Put some business logic here

        self.repository.create_expense(new_expense)
