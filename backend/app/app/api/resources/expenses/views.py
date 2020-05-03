from typing import Any

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api import deps
from app import crud, schemas
from .exeptions import ExpenseNotFoundExeption

router = APIRouter()


@router.post("/", response_model=schemas.Expense)
def create_expense(
    *,
    db: Session = Depends(deps.get_db),
    expense_in: schemas.ExpenseCreate
) -> Any:
    expense = crud.expense.create(db=db, obj_in=expense_in)

    return expense


@router.get("/{id}", response_model=schemas.Expense)
def get_expense(
    *,
    db: Session = Depends(deps.get_db),
    id: int
) -> Any:
    expense = crud.expense.get(db, id)

    if not expense:
        raise ExpenseNotFoundExeption

    return expense
