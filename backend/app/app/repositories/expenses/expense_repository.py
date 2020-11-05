from sqlalchemy.orm import Session

from app.adapters import expense_adapter
from app.entities.expenses import Expense
from app.infrastructure.db.models.expense import Expense as ExpenseModel
from app.interfaces.repositories.expense_repository import (
    AbstractExpenseRepository,
)


class ExpenseRepository(AbstractExpenseRepository):
    def __init__(self, db: Session):
        self.db = db

    def create_expense(self, expense: Expense) -> ExpenseModel:
        """Persist the expense on the database

        Args:
            expense (Expense): The Expense entity object

        Returns:
            Expenss: Returns the expense on the database
        """
        expense_model = expense_adapter.from_entity(expense)

        # Inserting into database
        self.db.add(expense_model)
        self.db.commit()
        self.db.refresh(expense_model)

        return expense_model

    def get_expense_by_id(self, id: int) -> Expense:
        expense = (
            self.db.query(ExpenseModel).filter(ExpenseModel.id == id).first()
        )

        return expense
