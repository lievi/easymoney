import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.infrastructure.db.models.base import Base
from app.services.unit_of_work import AbstractUnitOfWork, SqlAlchemyUnitOfWork


@pytest.fixture
def in_memory_sqlite_db():
    engine = create_engine('sqlite:///:memory:')
    Base.metadata.create_all(engine)
    return engine


@pytest.fixture
def sqlite_session_factory(in_memory_sqlite_db):
    yield sessionmaker(bind=in_memory_sqlite_db)


@pytest.fixture
def sqlalchemy_uow(sqlite_session_factory: sessionmaker) -> AbstractUnitOfWork:
    return SqlAlchemyUnitOfWork(sqlite_session_factory)
