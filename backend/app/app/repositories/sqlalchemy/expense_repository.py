from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from entities.expenses import Expense
from interfaces.repositories.expense_repository import (
    AbstractExpenseRepository,
)
from models.expense import Expense as SqlExpense


class ExpenseRepository(AbstractExpenseRepository):
    def __init__(self, db: Session):
        self.db = db

    def create_expense(self, expense: Expense) -> None:
        # TODO: Remove this comments later

        # creating an json with the entity
        obj_in_data = jsonable_encoder(expense)

        # Instantiating the base sqlalquemy class
        db_obj = SqlExpense(**obj_in_data)

        # Putting into the database
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def get_expense_by_id(self, id):
        pass
