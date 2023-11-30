import pytest
from pydantic import ValidationError
from sqlalchemy.orm import sessionmaker

from app.domain.expense import ExpenseCreation, ExpenseUpdate
from app.repositories.expense import SqlModelExpenseRepository


class TestSqlModelExpenseRepository:
    def test_expense_creation(
        self,
        sqlite_session_factory: sessionmaker,
        expense_create_entity: ExpenseCreation,
    ) -> None:
        session = sqlite_session_factory()
        repo = SqlModelExpenseRepository(session=session)
        saved_entity = repo.create(expense_create_entity)

        assert saved_entity.name == expense_create_entity.name
        assert saved_entity.value == expense_create_entity.value
        assert saved_entity.description == expense_create_entity.description

    def test_get_expense_create(
        self,
        sqlite_session_factory: sessionmaker,
        expense_create_entity: ExpenseCreation,
    ) -> None:
        session = sqlite_session_factory()
        repo = SqlModelExpenseRepository(session=session)
        saved_entity = repo.create(expense_create_entity)
        session.commit()

        entity = repo.get(saved_entity.id)

        assert entity is not None
        assert entity.name == expense_create_entity.name
        assert entity.value == expense_create_entity.value
        assert entity.description == expense_create_entity.description

    def test_update_expense(
        self,
        sqlite_session_factory: sessionmaker,
        expense_create_entity: ExpenseCreation,
    ) -> None:
        session = sqlite_session_factory()
        repo = SqlModelExpenseRepository(session=session)
        saved_entity = repo.create(expense_create_entity)
        session.commit()

        update_expense_model = ExpenseUpdate(value=20.4)  # type: ignore

        entity = repo.update(saved_entity.id, update_expense_model)

        assert entity is not None
        assert entity.name == expense_create_entity.name
        assert entity.value == 20.4
        assert entity.description == expense_create_entity.description

    def test_update_inexistent_expense(
        self,
        sqlite_session_factory: sessionmaker,
    ) -> None:
        session = sqlite_session_factory()
        repo = SqlModelExpenseRepository(session=session)

        update_expense_model = ExpenseUpdate(value=20.4)  # type: ignore

        entity = repo.update(1, update_expense_model)
        assert entity is None

    def test_update_expense_specifying_a_null_value_should_raise_exception(
        self,
    ) -> None:
        with pytest.raises(ValidationError) as err:
            ExpenseUpdate(value=20.4, name=None)  # type: ignore
        
        assert err.value.errors()[0]["msg"] == "The value should not be None"
