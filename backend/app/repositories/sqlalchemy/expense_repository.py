from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from entities.expenses import Expense
from interfaces.repositories.expense_repository import (
    AbstractExpenseRepository,
)


class ExpenseRepository(AbstractExpenseRepository):
    def __init__(self, db: Session):
        self.db = db

    def create_expense(self, expense: Expense) -> None:
        obj_in_data = jsonable_encoder(expense)
        db_obj = self.model(**obj_in_data)
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj
