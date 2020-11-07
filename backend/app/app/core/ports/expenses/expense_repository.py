from abc import ABC, abstractmethod
from typing import Any

from app.core.entities.expense import Expense, ExpenseCreate


class ExpenseRepository(ABC):
    @abstractmethod
    def create(self: ExpenseCreate) -> Expense:
        ...

    def get(self, id: Any) -> Expense:
        ...
