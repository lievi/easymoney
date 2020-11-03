from app.entities.expenses import Expense
from app.interfaces.repositories.expense_repository import (
    AbstractExpenseRepository
)


class FakeExpenseRepository(AbstractExpenseRepository):
    PAYLOAD = {
        'id': 1,
        'name': 'Fake Expense',
        'value': 1.0,
        'description': 'A fake expense'
    }

    def create_expense(self, expense: Expense) -> Expense:
        return self.PAYLOAD

    def get_expense_by_id(self, id: int) -> Expense:
        fake_expense = Expense(
            name=self.PAYLOAD['name'],
            value=self.PAYLOAD['value'],
            description=self.PAYLOAD['description']
        )

        fake_expense.id = self.PAYLOAD['id']

        return fake_expense
