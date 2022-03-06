from fastapi.testclient import TestClient

from app.db.session import engine
from app.config import settings
from app.domain.expense import ExpenseCreate
from app.services.expenses import create_expense
from app.services.unit_of_work import AbstractUnitOfWork


class TestExpenseAPI:
    def test_get_expense(
        self,
        client: TestClient,
        uow: AbstractUnitOfWork,
        expense_create_entity: ExpenseCreate,
        wait_dependencies: None # TODO: verify how improve this
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

    def test_expense_not_found(
        self,
        client: TestClient,
        uow: AbstractUnitOfWork,
        expense_create_entity: ExpenseCreate,
        wait_dependencies: None # TODO: verify how improve this
    ) -> None:
        response = client.get(
            f'{settings.API_V1_STR}/expenses/999'
        )
        assert response.status_code == 404
        content = response.json()
        content['detail'] = 'Item not found'


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
