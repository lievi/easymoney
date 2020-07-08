# TODO implement typing
from typing import Any
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from adapters.expenses import db_model_to_entity
from entities.expenses import Expense as Expense
from interfaces.repositories.expense_repository import (
    AbstractExpenseRepository,
)
from infrastructure.db.models.expense import Expense as ExpenseDB


class ExpenseRepository(AbstractExpenseRepository):
    def __init__(self, db: Session):
        self.db = db
        self.expense_model = ExpenseDB

    def create_expense(self, expense: Expense) -> None:
        # creating an json with the entity
        obj_in_data = jsonable_encoder(expense)

        # Instantiating the base sqlalquemy class
        db_obj = ExpenseDB(**obj_in_data)

        # Putting into the database
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def get_expense_by_id(self, id: Any) -> Expense:
        expense_from_db = (
            self.db.query(self.expense_model)
            .filter(self.expense_model.id == id)
            .first()
        )
        return db_model_to_entity(expense_from_db)
