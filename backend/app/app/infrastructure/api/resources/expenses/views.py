from typing import Any

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.entities.expense import Expense, ExpenseCreate
from app.infrastructure.api import dependencies
from app.adapters.expense.expense_repository import ExpenseRepositoryAdapter
from app.core.use_cases.expenses import expenses_use_case

from .exceptions import ExpenseNotFoundExeption

router = APIRouter()


@router.post("/", response_model=Expense)
def create_expense(
    *,
    db: Session = Depends(dependencies.get_db),
    expense: ExpenseCreate,
) -> Any:
    # Instantiating the repository to persist the data
    # TODO: Verify how to change this adapter on config(maybe a factory?)
    # TODO: clone the repository of the tiangolo and verify if the CRUD class
    # is instantiated on every request (put a log)
    repository = ExpenseRepositoryAdapter()

    # Executing the use case with all the logic needed
    use_case = expenses_use_case.CreateExpense(repository)
    new_expense = use_case.execute(expense, db)

    # Returning the data
    return new_expense


@router.get("/{id}", response_model=Expense)
def get_expense(*, db: Session = Depends(dependencies.get_db), id: int) -> Any:
    # Instantiating the repository to get the data
    repository = ExpenseRepositoryAdapter()

    # Executing the usecase
    use_case = expenses_use_case.GetExpenseById(repository)
    expense = use_case.execute(id, db)

    # TODO: Put this logic on the usecase
    if not expense:
        raise ExpenseNotFoundExeption

    return expense
