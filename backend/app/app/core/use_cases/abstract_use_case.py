from abc import ABC, abstractmethod
from app.core.ports.expenses.expense_repository import (
    ExpenseRepository
)


class AbstractUseCase(ABC):
    @abstractmethod
    def __init__(self, repository: ExpenseRepository):
        ...

    @abstractmethod
    def execute(self) -> None:
        ...
