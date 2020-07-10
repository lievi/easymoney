from typing import Any

from sqlalchemy.orm import Session

from entities.expenses import Expense as Expense
from infrastructure.db.adapters.expenses import ExpenseDBAdapter
from infrastructure.db.models.expense import Expense as ExpenseModel
from interfaces.repositories.expense_repository import (
    AbstractExpenseRepository,
)


class ExpenseRepository(AbstractExpenseRepository):
    def __init__(self, db: Session):
        self.db = db

    def create_expense(self, expense: Expense) -> None:
        expense_model = ExpenseDBAdapter.from_entity(expense)

        # Inserting into database
        self.db.add(expense_model)
        self.db.commit()
        self.db.refresh(expense_model)
        return expense_model

    def get_expense_by_id(self, id: Any) -> Expense:
        expense_from_db = (
            self.db.query(ExpenseModel).filter(ExpenseModel.id == id).first()
        )
        expense = ExpenseDBAdapter.to_entity(expense_from_db)
        return expense