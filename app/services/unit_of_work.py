from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any

from sqlalchemy.orm import sessionmaker, Session

from app.adapters.repositories.expense import (
    AbstractExpenseRepository,
    FakeExpenseRepository,
    SqlAlchemyExpenseRepository,
)
from app.infrastructure.db.session import SessionLocal


class AbstractUnitOfWork(ABC):
    expenses: AbstractExpenseRepository

    def __enter__(self) -> None:
        return self

    def __exit__(self, *args: Any) -> None:
        self.rollback()

    @abstractmethod
    def commit(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def rollback(self) -> None:
        raise NotImplementedError


class FakeUnitOfWork(AbstractUnitOfWork):
    expenses = FakeExpenseRepository()

    def commit(self) -> None:
        pass  # pragma: no cover

    def rollback(self) -> None:
        pass


class SqlAlchemyUnitOfWork(AbstractUnitOfWork):
    def __init__(self, session_factory: sessionmaker = SessionLocal) -> None:
        self.session_factory: sessionmaker = session_factory

    def __enter__(self) -> None:
        self.session: Session = self.session_factory()
        self.expenses = SqlAlchemyExpenseRepository(self.session)
        super().__enter__()

    def __exit__(self, *args: Any) -> None:
        super().__exit__(*args)
        self.session.close()

    def commit(self) -> None:
        self.session.commit()

    def rollback(self) -> None:
        self.session.rollback()
