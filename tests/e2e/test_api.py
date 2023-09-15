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
        expense_repository: ExpensesRepository,
        expense_create_entity: CreateExpenseSchema,
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
