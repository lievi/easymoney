from sqlalchemy.orm import Session

from app.core.entities.expense import ExpenseCreate
from app.core.ports.expenses.expense_repository import ExpenseRepository
from app.infrastructure.db.base_repository import CRUDBase
from app.infrastructure.db.models.expense import Expense


class ExpenseRepositoryAdapter(CRUDBase[Expense, ExpenseCreate]):
    ...
    def __init__(self):
        super().__init__(model=Expense)
