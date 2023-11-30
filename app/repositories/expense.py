from abc import ABC, abstractmethod

from sqlmodel import Session

from app.db.sqlmodel.orm import ExpenseDB
from app.domain.expense import Expense, ExpenseCreation, ExpenseUpdate


class ExpensesRepository(ABC):
    @abstractmethod
    def create(self, expense: ExpenseCreation) -> Expense:
        raise NotImplementedError

    @abstractmethod
    def get(self, id: int) -> Expense | None:
        raise NotImplementedError

    @abstractmethod
    def update(self, id: int, update_payload: ExpenseUpdate) -> Expense | None:
        raise NotImplementedError


class FakeExpenseRepository(ExpensesRepository):
    def __init__(self) -> None:
        self._expenses: list[Expense] = list()

    def create(self, expense: ExpenseCreation) -> Expense:
        new_expense = Expense(id=1, **expense.dict())
        self._expenses.append(new_expense)
        return new_expense

    def get(self, id: int) -> Expense | None:
        return next((e for e in self._expenses if e.id == id), None)

    def update(self, id: int, update_payload: ExpenseUpdate) -> Expense | None:
        expense_index = next(
            (index for index, e in enumerate(self._expenses) if e.id == id),
            None,
        )

        if expense_index is None:
            return None

        for key, value in update_payload.dict().items():
            setattr(self._expenses[expense_index], key, value)

        return self._expenses[expense_index]


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

    def update(self, id: int, update_payload: ExpenseUpdate) -> Expense | None:
        expense = self.session.get(ExpenseDB, id, with_for_update=True)
        if not expense:
            return None

        for key, value in update_payload.dict(exclude_none=True).items():
            setattr(expense, key, value)

        self.session.add(expense)
        self.session.commit()
        self.session.refresh(expense)

        return Expense(**expense.dict())
