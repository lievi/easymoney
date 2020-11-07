from app.core.entities.expense import Expense, ExpenseCreate
from app.core.ports.expenses.expense_repository import ExpenseRepository


class FakeExpenseRepositoryAdapter(ExpenseRepository):
    PAYLOAD = {
        'id': 1,
        'name': 'Fake Expense',
        'value': 1.0,
        'description': 'A fake expense'
    }

    def create(self, expense: ExpenseCreate) -> Expense:
        return Expense(
            **expense
        )

    def get_expense_by_id(self, id: int) -> Expense:
        fake_expense = Expense(
            id=self.PAYLOAD['id'],
            name=self.PAYLOAD['name'],
            value=self.PAYLOAD['value'],
            description=self.PAYLOAD['description']
        )

        return fake_expense
