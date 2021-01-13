from fastapi.testclient import TestClient

from app.config import settings
from app.domain.expense import ExpenseCreate
from app.services.expense import create_expense
from app.services.unit_of_work import AbstractUnitOfWork


class TestExpenseAPI:
    def test_get_expense(
        self,
        client: TestClient,
        uow: AbstractUnitOfWork,
        expense_create_entity: ExpenseCreate
    ) -> None:
        expected_expense = create_expense(uow, expense_create_entity)

        response = client.get(
            f'{settings.API_V1_STR}/expenses/{expected_expense.id}'
        )
        assert response.status_code == 200
        expense = response.json()

        assert 'id' in expense
        assert expense['name'] == expected_expense.name
        assert expense['value'] == expected_expense.value
        assert expense['description'] == expected_expense.description

    def test_create_expense(
        self,
        client: TestClient,
        uow: AbstractUnitOfWork,
        expense_create_payload: dict
    ) -> None:
        response = client.post(
            f'{settings.API_V1_STR}/expenses/', json=expense_create_payload
        )
        assert response.status_code == 200
        expense = response.json()

        assert 'id' in expense
        assert expense['name'] == expense_create_payload['name']
        assert expense['value'] == expense_create_payload['value']
        assert expense['description'] == expense_create_payload['description']
