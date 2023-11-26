import logging
from typing import Any

from fastapi import APIRouter, Depends
from sqlmodel import Session

from app.api.dependencies import db_session
from app.repositories.expense import (
    SqlAlchemyExpenseRepository,
    SqlModelExpenseRepository,
)
from app.services import expenses as service
from app.services.exceptions import ExpenseNotFound

from .exceptions import ItemNotFound
from .schemas import CreateExpenseSchema, ExpenseSchema

logger = logging.getLogger(__name__)
router = APIRouter()


@router.post("/", response_model=ExpenseSchema)
def create_expense(
    *,
    db_session: Session = Depends(db_session),
    expense: CreateExpenseSchema,
) -> Any:
    # Instantiating the repository to persist the data
    # TODO: How to dynamically get the repo class
    repo = SqlModelExpenseRepository(db_session)

    # Executing the use case with all the logic needed
    new_expense = service.create_expense(repo, expense)

    # Returning the data
    return new_expense


@router.get(
    "/{id}",
    response_model=ExpenseSchema,
    responses={404: ItemNotFound().open_api_doc()},
)
def get_expense(
    *, id: int, db_session: Session = Depends(db_session)
) -> ExpenseSchema:
    repo = SqlModelExpenseRepository(db_session)
    try:
        expense = service.get_by_id(repo, id)
    except ExpenseNotFound as e:
        raise ItemNotFound(e.detail) from e
    expense = ExpenseSchema(**expense.dict())
    return expense
