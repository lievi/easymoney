import logging

from typing import Any

from fastapi import APIRouter, Request

from app.services import expense as service
from app.services.exceptions import ExpenseNotFound
from app.services.unit_of_work import SqlAlchemyUnitOfWork
from app.domain.expense import Expense, ExpenseCreate


logger = logging.getLogger(__name__)
router = APIRouter()


@router.post("/", response_model=Expense)
def create_expense(
    *, expense: ExpenseCreate,
) -> Any:
    # Instantiating the repository to persist the data
    uow = SqlAlchemyUnitOfWork() # TODO: verify how to inject this dependency

    # Executing the use case with all the logic needed
    new_expense = service.create_expense(uow, expense)

    # Returning the data
    return new_expense


@router.get("/{id}", response_model=Expense)
def get_expense(*, id: int) -> Any:
    # Instantiating the UOW to get the data
    # TODO: Verify how to create a bootstrap to put this instantiation
    uow = SqlAlchemyUnitOfWork()

    # Executing the usecase
    expense = service.get_by_id(uow, id)

    return expense


# @router.exception_handler(ExpenseNotFound)
# def unicorn_exception_handler(request: Request, exc: ExpenseNotFound):
#     return JSONResponse(
#         status_code=418,
#         content={"message": f"Oops! {exc.name} did something. There goes a rainbow..."},
#     )
