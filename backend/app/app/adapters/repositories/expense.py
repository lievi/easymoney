from abc import ABC, abstractmethod
from typing import Any

from app.domain.expense import Expense, ExpenseCreate
from app.infrastructure.db.base_crud import CRUDBase
from app.infrastructure.db.models.expense import Expense as ExpenseModel


class AbstractExpenseRepository(ABC):
    @abstractmethod
    def create(self, expense: ExpenseCreate) -> Expense:
        ...

    def get(self, id: Any) -> Expense:
        ...


class FakeExpenseRepository(AbstractExpenseRepository):
    PAYLOAD = {
        'id': 1,
        'name': 'Fake Expense',
        'value': 1.0,
        'description': 'A fake expense',
    }

    def create(self, expense: ExpenseCreate) -> Expense:
        return Expense(**expense)

    def get(self, id: int) -> Expense:
        fake_expense = Expense(
            id=self.PAYLOAD['id'],
            name=self.PAYLOAD['name'],
            value=self.PAYLOAD['value'],
            description=self.PAYLOAD['description'],
        )

        return fake_expense


# this will be a problem
class SqlAlchemyExpenseRepository(
    CRUDBase[ExpenseModel, ExpenseCreate], AbstractExpenseRepository
):
    ...
