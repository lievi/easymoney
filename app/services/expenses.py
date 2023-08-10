from app.domain.expense import Expense, ExpenseCreate
from app.services.unit_of_work import AbstractUnitOfWork

from .exceptions import ExpenseNotFound


def create_expense(uow: AbstractUnitOfWork, expense: ExpenseCreate) -> Expense:
    with uow:
        new_expense = uow.expenses.create(expense)
        uow.commit()
        return Expense.from_orm(new_expense)


def get_by_id(uow: AbstractUnitOfWork, expense_id: int) -> Expense:
    with uow:
        db_expense = uow.expenses.get(expense_id)
        if not db_expense:
            raise ExpenseNotFound
        return Expense.from_orm(db_expense)
