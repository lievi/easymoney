from abc import ABC, abstractmethod

from sqlalchemy.orm import Session as SqlAlchemySession
from sqlmodel import Session

from app.db.sqlalchemy.base_crud import CRUDBase
from app.db.sqlalchemy.orm.expense import Expense as ExpenseOrm
from app.db.sqlmodel.orm import ExpenseDB
from app.domain.expense import Expense, ExpenseCreation


class ExpensesRepository(ABC):
    @abstractmethod
    def create(self, expense: ExpenseCreation) -> Expense:
        raise NotImplementedError

    @abstractmethod
    def get(self, id: int) -> Expense:
        raise NotImplementedError


class FakeExpenseRepository(ExpensesRepository):
    def __init__(self) -> None:
        self._expenses: list[Expense] = list()

    def create(self, expense: ExpenseCreation) -> Expense:
        new_expense = Expense(id=1, **expense.dict())
        self._expenses.append(new_expense)
        return new_expense

    def get(self, id: int) -> Expense:
        return next((e for e in self._expenses if e.id == id), None)


class SqlAlchemyExpenseRepository(
    CRUDBase[ExpenseOrm, ExpenseCreation], ExpensesRepository
):
    def __init__(self, db: SqlAlchemySession):
        super().__init__(ExpenseOrm, db)

    ...


class SqlModelExpenseRepository(ExpensesRepository):
    def __init__(self, session: Session) -> None:
        self.session = session
        super().__init__()

    def create(self, expense: ExpenseCreation) -> Expense:
        expense_db = ExpenseDB.from_orm(expense)

        self.session.add(expense_db)
        self.session.commit()
        self.session.refresh(expense_db)
        return Expense(**expense_db.dict())

    def get(self, id: int) -> Expense | None:
        expense_db = self.session.get(ExpenseDB, id)
        return Expense.parse_obj(expense_db) if expense_db else None
