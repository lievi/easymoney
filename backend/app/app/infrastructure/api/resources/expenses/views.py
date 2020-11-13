from typing import Any

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.entities.expense import Expense, ExpenseCreate
from app.infrastructure.api import dependencies
from app.adapters.expense.expense_repository import expense_repository_adapter
from app.core.use_cases.expenses import expenses_use_case

from .exceptions import ExpenseNotFoundExeption

router = APIRouter()


@router.post("/", response_model=Expense)
def create_expense(
    *,
    expense: ExpenseCreate,
) -> Any:
    # Instantiating the repository to persist the data
    # TODO: Verify how to change this adapter on config(maybe a factory?)
    # TODO: clone the repository of the tiangolo and verify if the CRUD class
    # is instantiated on every request (put a log)
    repository = expense_repository_adapter

    # Executing the use case with all the logic needed
    use_case = expenses_use_case.CreateExpense(repository)
    new_expense = use_case.execute(expense)

    # Returning the data
    return new_expense


@router.get("/{id}", response_model=Expense)
def get_expense(id: int) -> Any:
    # Instantiating the repository to get the data
    repository = expense_repository_adapter

    # Executing the usecase
    use_case = expenses_use_case.GetExpenseById(repository)
    expense = use_case.execute(id)

    # TODO: Put this logic on the usecase
    if not expense:
        raise ExpenseNotFoundExeption

    return expense
