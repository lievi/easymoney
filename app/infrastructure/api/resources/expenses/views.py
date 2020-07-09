from typing import Any

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from infrastructure.api import dependencies
from infrastructure.db.repositories.expense_repository import ExpenseRepository
from use_cases import expenses_use_case

from .exeptions import ExpenseNotFoundExeption
from .schemas import ExpenseCreateSchema, ExpenseSchema

router = APIRouter()


@router.post("/", response_model=ExpenseSchema)
def create_expense(
    *,
    db: Session = Depends(dependencies.get_db),
    expense_in: ExpenseCreateSchema,
) -> Any:
    repository = ExpenseRepository(db)
    use_case = expenses_use_case.CreateExpense(repository)
    use_case.execute(expense_in.dict())


@router.get("/{id}", response_model=ExpenseSchema)
def get_expense(*, db: Session = Depends(dependencies.get_db), id: int) -> Any:
    repository = ExpenseRepository(db)
    use_case = expenses_use_case.GetExpenseById(repository)
    expense = use_case.execute(id)

    if not expense:
        raise ExpenseNotFoundExeption

    return expense
