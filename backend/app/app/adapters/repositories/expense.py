from abc import ABC, abstractmethod
from typing import Any, List

from sqlalchemy.orm import Session

from app.domain.expense import Expense, ExpenseCreate
from app.infrastructure.db.base_crud import CRUDBase
from app.infrastructure.db.models.expense import Expense as ExpenseModel


class AbstractExpenseRepository(ABC):
    @abstractmethod
    def create(self, expense: ExpenseCreate) -> Expense:
        raise NotImplementedError

    @abstractmethod
    def get(self, id: Any) -> Expense:
        raise NotImplementedError


class FakeExpenseRepository(AbstractExpenseRepository):
    def __init__(self) -> None:
        super().__init__()
        self._expenses: List[Expense] = list()

    def create(self, expense: ExpenseCreate) -> Expense:
        new_expense = Expense(id=1, **expense.dict())
        self._expenses.append(new_expense)
        return new_expense

    def get(self, id: int) -> Expense:
        return next(e for e in self._expenses if e.id == id)


class SqlAlchemyExpenseRepository(
    CRUDBase[ExpenseModel, Expense], AbstractExpenseRepository
):
    def __init__(self, db: Session):
        super().__init__(ExpenseModel, db)
    ...
