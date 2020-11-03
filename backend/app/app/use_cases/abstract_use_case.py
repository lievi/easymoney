# Verify if put it here
from abc import ABC, abstractmethod
from app.interfaces.repositories.expense_repository import (
    AbstractExpenseRepository,
)


class AbstractUseCase(ABC):
    @abstractmethod
    def __init__(self, repository: AbstractExpenseRepository):
        ...

    @abstractmethod
    def execute(self) -> None:
        ...
