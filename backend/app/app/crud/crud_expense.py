from app.crud.base import CRUDBase
from app.models.expense import Expense


class CRUDExpense(CRUDBase[Expense]):
    ...


expense = CRUDExpense(Expense)
