from typing import Any

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from .exceptions import ExpenseNotFoundExeption
from app.adapters.repositories.expense import SqlAlchemyExpenseRepository
from app.services import expense as service
from app.services.unit_of_work import SqlAlchemyUnitOfWork
from app.domain.expense import Expense, ExpenseCreate
from app.infrastructure.api import dependencies


router = APIRouter()


@router.post("/", response_model=Expense)
def create_expense(
    *, db: Session = Depends(dependencies.get_db), expense: ExpenseCreate,
) -> Any:
    # Instantiating the repository to persist the data
    repository = SqlAlchemyExpenseRepository(db)

    # Executing the use case with all the logic needed
    new_expense = service.create_expense(repository, expense)

    # Returning the data
    return new_expense


@router.get("/{id}", response_model=Expense)
def get_expense(*, id: int) -> Any:
    # Instantiating the UOW to get the data
    # TODO: Verify how to create a bootstrap to put this instantiation
    uow = SqlAlchemyUnitOfWork()

    # Executing the usecase
    expense = service.get_by_id(uow, id)

    # TODO: Put this logic on the usecase
    if not expense:
        raise ExpenseNotFoundExeption

    return expense
