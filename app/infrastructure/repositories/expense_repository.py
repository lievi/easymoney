# TODO implement typing
from typing import Any
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from entities.expenses import Expense as ExpenseEntity
from interfaces.repositories.expense_repository import (
    AbstractExpenseRepository,
)
from infrastructure.db.models.expense import Expense


class ExpenseRepository(AbstractExpenseRepository):
    def __init__(self, db: Session):
        self.db = db
        self.expense_model = Expense

    def create_expense(self, expense: Expense) -> None:
        # TODO: Remove this comments later

        # creating an json with the entity
        obj_in_data = jsonable_encoder(expense)

        # Instantiating the base sqlalquemy class
        db_obj = ExpenseEntity(**obj_in_data)

        # Putting into the database
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def get_expense_by_id(self, id: Any) -> ExpenseEntity:
        # FIXME transform the db expense on a entity expense
        # Create an adapter to that
        batata = (
            self.db.query(self.expense_model)
            .filter(self.expense_model.id == id)
            .first()
        )
        return batata
