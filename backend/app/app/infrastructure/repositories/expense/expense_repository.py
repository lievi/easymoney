from sqlalchemy.orm import Session

from app.entities.expenses import Expense as Expense
from app.infrastructure.db.adapters.expenses import ExpenseDBAdapter
from app.infrastructure.db.models.expense import Expense as ExpenseModel
from app.interfaces.repositories.expense_repository import (
    AbstractExpenseRepository,
)


class ExpenseRepository(AbstractExpenseRepository):
    def __init__(self, db: Session):
        self.db = db

    def create_expense(self, expense: Expense) -> int:
        """Persist the expense on the database

        Args:
            expense (Expense): The Expense entity object

        Returns:
            int: Returns the id of row on the database
        """
        expense_model = ExpenseDBAdapter.from_entity(expense)

        # Inserting into database
        self.db.add(expense_model)
        self.db.commit()
        self.db.refresh(expense_model)
        return expense_model.id

    def get_expense_by_id(self, id: int) -> Expense:
        expense_from_db = (
            self.db.query(ExpenseModel).filter(ExpenseModel.id == id).first()
        )
        expense = ExpenseDBAdapter.to_entity(expense_from_db)
        return expense
