from fastapi import HTTPException
from starlette import status


class ExpenseNotFoundExeption(HTTPException):
    def __init__(self) -> None:
        self.status_code = status.HTTP_404_NOT_FOUND
        self.detail = 'Expense not found'
