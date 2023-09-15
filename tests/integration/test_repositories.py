from sqlalchemy.orm import sessionmaker
from app.repositories.expense import SqlAlchemyExpenseRepository
from app.domain.expense import ExpenseCreation


class TestSqlAlchemyExpenseRepository:
    def test_expense_creation(
        self,
        sqlite_session_factory: sessionmaker,
        expense_create_entity: ExpenseCreation,
    ) -> None:
        session = sqlite_session_factory()
        repo = SqlAlchemyExpenseRepository(db=session)
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
        repo = SqlAlchemyExpenseRepository(db=session)
        saved_entity = repo.create(expense_create_entity)
        session.commit()

        entity = repo.get(saved_entity.id)

        assert entity.name == expense_create_entity.name
        assert entity.value == expense_create_entity.value
        assert entity.description == expense_create_entity.description
