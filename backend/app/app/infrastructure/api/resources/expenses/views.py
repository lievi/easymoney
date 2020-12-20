from typing import Any

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from .exceptions import ExpenseNotFoundExeption
from app.adapters.repositories.expense import SqlAlchemyExpenseRepository
from app.services import expense as service
from app.domain.expense import Expense, ExpenseCreate
from app.infrastructure.db.models.expense import Expense as ExpenseModel
from app.infrastructure.api import dependencies


router = APIRouter()


@router.post("/", response_model=Expense)
def create_expense(
    *, db: Session = Depends(dependencies.get_db), expense: ExpenseCreate,
) -> Any:
    # Instantiating the repository to persist the data
    repository = SqlAlchemyExpenseRepository(ExpenseModel, db)

    # Executing the use case with all the logic needed
    new_expense = service.create_expense(repository, expense)

    # Returning the data
    return new_expense


@router.get("/{id}", response_model=Expense)
def get_expense(*, db: Session = Depends(dependencies.get_db), id: int) -> Any:
    # Instantiating the repository to get the data
    repository = SqlAlchemyExpenseRepository(ExpenseModel, db)

    # Executing the usecase
    expense = service.get_by_id(repository, id)

    # TODO: Put this logic on the usecase
    if not expense:
        raise ExpenseNotFoundExeption

    return expense
