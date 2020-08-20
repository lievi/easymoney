from typing import Any
from abc import ABC, abstractmethod

from app.entities.expenses import Expense


class AbstractExpenseRepository(ABC):
    @abstractmethod
    def get_expense_by_id(self, id: Any) -> Expense:
        """ Get an expense entity by the id

        Args:
            id (Any): The id of the expense

        Returns:
            Returns the expense
        """

    @abstractmethod
    def create_expense(self, expense: Expense) -> None:
        """ Persists a new expense

        Args:
            expense (Expense): A new expense to be persisted
        """
