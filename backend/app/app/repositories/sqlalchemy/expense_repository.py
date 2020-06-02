from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from entities.expenses import Expense
from interfaces.repositories.expense_repository import (
    AbstractExpenseRepository,
)
from adapters.expenses import Expense as ExpenseAdapter


class ExpenseRepository(AbstractExpenseRepository):
    def __init__(self, db: Session):
        self.db = db

    def create_expense(self, expense: Expense) -> None:
        obj_in_data = jsonable_encoder(expense)
        import ipdb; ipdb.set_trace()
        db_obj = ExpenseAdapter(**obj_in_data)
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def get_expense_by_id(self, id):
        pass
