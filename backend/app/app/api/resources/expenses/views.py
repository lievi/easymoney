from typing import Any

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api import deps

# from app import crud, schemas
from .exeptions import ExpenseNotFoundExeption

# FIX: Sera?
# from .models import expense_model
from adapters import expenses as expense_adapters
from use_cases import expenses_use_case
from repositories.sqlalchemy.expense_repository import ExpenseRepository

router = APIRouter()


@router.post("/", response_model=expense_adapters.Expense)
def create_expense(
    *,
    db: Session = Depends(deps.get_db),
    expense_in: expense_adapters.ExpenseCreate,
) -> Any:
    # expense = expense_model.create(db=db, obj_in=expense_in)
    # return expense
    repository = ExpenseRepository(db)
    uc = expenses_use_case.CreateExpense(repository)
    print(expense_in.dict())
    uc.execute(**expense_in.dict())


@router.get("/{id}", response_model=expense_adapters.Expense)
def get_expense(*, db: Session = Depends(deps.get_db), id: int) -> Any:
    expense = expense_model.get(db, id)

    if not expense:
        raise ExpenseNotFoundExeption

    return expense
