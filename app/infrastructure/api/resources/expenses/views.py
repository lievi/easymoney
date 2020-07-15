from typing import Any

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from infrastructure.api import dependencies
from infrastructure.repositories.expense_repository import ExpenseRepository
from use_cases import expenses_use_case

from .adapters import ExpenseAdapter
from .exeptions import ExpenseNotFoundExeption
from .schemas import ExpenseOutputSchema, ExpenseSchema

router = APIRouter()


@router.post("/", response_model=ExpenseOutputSchema)
def create_expense(
    *,
    db: Session = Depends(dependencies.get_db),
    expense_in: ExpenseSchema,
) -> Any:
    # Adapting the schema received to an entity
    expense = ExpenseAdapter.to_entity(expense_in)

    # Instantiating the repository to persist the data
    repository = ExpenseRepository(db)

    # Executing the use case with all the logic needed
    use_case = expenses_use_case.CreateExpense(repository)
    saved_expense = use_case.execute(expense)

    # Adapting the saved entity to an output schema
    output_expense = ExpenseAdapter.from_entity(saved_expense)

    # Returning the data
    return output_expense


@router.get("/{id}", response_model=ExpenseOutputSchema)
def get_expense(*, db: Session = Depends(dependencies.get_db), id: int) -> Any:
    # Instantiating the repository to get the data
    repository = ExpenseRepository(db)

    # Executing the usecase
    use_case = expenses_use_case.GetExpenseById(repository)
    expense = use_case.execute(id)

    # Adapting the entity to the output schema
    output_expense = ExpenseAdapter.from_entity(expense)

    # TODO: Put this logic on the usecase
    if not expense:
        raise ExpenseNotFoundExeption

    return output_expense
