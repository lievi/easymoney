from sqlalchemy.orm import sessionmaker, Session

from app.domain.expense import Expense
from app.services.unit_of_work import SqlAlchemyUnitOfWork


class TestSqlAlchemyUnitOfWork:
    def add_expense_on_db(
        self, session: Session, expense_create_payload: dict
    ) -> None:
        session.execute(
            (
                'INSERT INTO expense (id, name, value)'
                'VALUES (:id, :name, :value)'
            ),
            expense_create_payload,
        )

    def test_get_expense(
        self,
        sqlite_session_factory: sessionmaker,
        expense_create_payload: dict,
    ) -> None:
        expected_id = 1
        expense_create_payload['id'] = expected_id

        session = sqlite_session_factory()
        self.add_expense_on_db(
            session, expense_create_payload
        )
        session.commit()
        session.close()

        uow = SqlAlchemyUnitOfWork(sqlite_session_factory)

        with uow:
            expense = uow.expenses.get(expected_id)

            assert expense.id == expected_id
            assert expense.name == expense_create_payload['name']
            assert expense.value == expense_create_payload['value']
