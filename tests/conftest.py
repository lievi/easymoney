import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from easymoney.api.expenses.schemas import CreateExpenseSchema
from easymoney.db.sqlmodel.orm import ExpenseDB
from easymoney.domain.expense import Expense
from easymoney.repositories.expense import ExpensesRepository, FakeExpenseRepository


@pytest.fixture
def expense_create_payload() -> dict:
    return {
        'name': 'fake expense',
        'value': 2.0,
        'description': 'fake description'
    }


@pytest.fixture
def expense_entity() -> Expense:
    return Expense(
        id=1,
        name='fake expense',
        value=2.0,
        description='fake description'
    )


@pytest.fixture
def expense_create_entity() -> CreateExpenseSchema:
    return CreateExpenseSchema(
        name='fake expense',
        value=2.0,
        description='fake description'
    )

@pytest.fixture
def in_memory_sqlite_db():
    engine = create_engine('sqlite:///:memory:')
    ExpenseDB.metadata.create_all(engine)
    return engine

@pytest.fixture
def sqlite_session_factory(in_memory_sqlite_db):
    yield sessionmaker(bind=in_memory_sqlite_db)
