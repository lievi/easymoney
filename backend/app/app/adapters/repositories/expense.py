from abc import ABC, abstractmethod
from typing import Any, Set
from uuid import uuid4

from app.domain.expense import Expense, ExpenseInDb
from app.infrastructure.db.base_crud import CRUDBase
from app.infrastructure.db.models.expense import Expense as ExpenseModel


class AbstractExpenseRepository(ABC):
    @abstractmethod
    def create(self, expense: Expense) -> ExpenseInDb:
        ...

    @abstractmethod
    def get(self, id: Any) -> Expense:
        ...


class FakeExpenseRepository(AbstractExpenseRepository):
    def __init__(self) -> None:
        self._expenses: Set[Expense] = set()
        super().__init__()

    def create(self, expense: Expense) -> ExpenseInDb:
        # self._expenses.
        new_expense = Expense(id=1, **expense.dict())
        self._expenses.add(new_expense)
        return new_expense

    def get(self, id: int) -> ExpenseInDb:
        return next(e for e in self._expenses if e.id == id)


class SqlAlchemyExpenseRepository(
    CRUDBase[ExpenseModel, Expense], AbstractExpenseRepository
):
    ...
