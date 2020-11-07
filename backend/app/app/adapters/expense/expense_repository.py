from sqlalchemy.orm import Session

from app.core.entities.expense import Expense, ExpenseCreate
from app.core.ports.expenses.expense_repository import ExpenseRepository
from app.infrastructure.db.base_repository import CRUDBase


class ExpenseRepositoryAdapter(
    ExpenseRepository, CRUDBase[Expense, ExpenseCreate]
):
    def __init__(self, db: Session):
        self.db = db
