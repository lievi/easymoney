from fastapi.testclient import TestClient

from app.api.dependencies import get_session
from app.api.expenses.schemas import CreateExpenseSchema, ExpenseSchema
from app.config import settings
from app.domain.expense import ExpenseCreation
from app.repositories.expense import ExpensesRepository
from app.services.expenses import create_expense


# TODO: check how to check dependencies
class TestExpenseAPI:
    def test_get_expense(
        self,
        client: TestClient,
        expense_create_entity: CreateExpenseSchema,
        expense_repository: ExpensesRepository,
    ) -> None:
        new_expense = ExpenseCreation(**expense_create_entity.dict())
        expected_expense = create_expense(expense_repository, new_expense)

        response = client.get(
            f"{settings.API_V1_STR}/expenses/{expected_expense.id}"
        )
        assert response.status_code == 200
        expense = response.json()

        assert "id" in expense
        assert expense["name"] == expected_expense.name
        assert expense["value"] == expected_expense.value
        assert expense["description"] == expected_expense.description

    def test_expense_not_found(
        self,
        client: TestClient,
    ) -> None:
        response = client.get(f"{settings.API_V1_STR}/expenses/999")
        assert response.status_code == 404
        content = response.json()
        content["detail"] = "Item not found"

    def test_create_expense(
        self,
        client: TestClient,
        expense_create_payload: dict,
    ) -> None:
        response = client.post(
            f"{settings.API_V1_STR}/expenses/", json=expense_create_payload
        )
        assert response.status_code == 200
        expense = response.json()
        assert "id" in expense
        assert expense["name"] == expense_create_payload["name"]
        assert expense["value"] == expense_create_payload["value"]
        assert expense["description"] == expense_create_payload["description"]

    def test_update_expense(
        self,
        client: TestClient,
        expense_repository: ExpensesRepository,
        expense_create_entity: CreateExpenseSchema,
        expense_create_payload: dict,
    ) -> None:
        new_expense = ExpenseCreation(**expense_create_entity.dict())
        expense = create_expense(expense_repository, new_expense)
        expense_create_payload["name"] = "updated expense"

        response = client.put(
            f"{settings.API_V1_STR}/expenses/{expense.id}",
            json=expense_create_payload
        )

        expense_create_payload["id"] = expense.id
        assert response.status_code == 200
        assert response.json() == expense_create_payload

    def test_update_with_none_value_should_return_unprocessable_entity(
        self,
        client: TestClient,
        expense_repository: ExpensesRepository,
        expense_create_entity: CreateExpenseSchema,
        expense_create_payload: dict,
    ) -> None:
        new_expense = ExpenseCreation(**expense_create_entity.dict())
        expense = create_expense(expense_repository, new_expense)
        expense_create_payload["name"] = None

        response = client.put(
            f"{settings.API_V1_STR}/expenses/{expense.id}",
            json=expense_create_payload
        )

        assert response.status_code == 422
        assert response.json()['detail'][0]['loc'] == ["body", "name"]


    def test_update_with_missing_field_should_return_unprocessable_entity(
        self,
        client: TestClient,
        expense_repository: ExpensesRepository,
        expense_create_entity: CreateExpenseSchema,
        expense_create_payload: dict,
    ) -> None:
        new_expense = ExpenseCreation(**expense_create_entity.dict())
        expense = create_expense(expense_repository, new_expense)
        del expense_create_payload["name"]

        response = client.put(
            f"{settings.API_V1_STR}/expenses/{expense.id}",
            json=expense_create_payload
        )

        assert response.status_code == 422
        assert response.json()['detail'][0]['loc'] == ["body", "name"]

    def test_expense_not_found_when_trying_to_update(
        self,
        client: TestClient,
        expense_create_payload: dict,
    ) -> None:
        response = client.put(
            f"{settings.API_V1_STR}/expenses/999",
            json=expense_create_payload
        )

        assert response.status_code == 404
        assert response.json()["detail"] == "Expense not found"

class TestHealthcheck:
    def test_should_return_pong(self, client: TestClient):
        response = client.get(f"{settings.API_V1_STR}/ping")
        assert response.status_code == 200
        assert response.json() == "pong"
