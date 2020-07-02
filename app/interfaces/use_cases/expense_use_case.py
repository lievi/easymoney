# Verify if put it here
from abc import ABC, abstractmethod
from interfaces.repositories.expense_repository import (
    AbstractExpenseRepository,
)


class AbstractExpenseUseCase(ABC):
    @abstractmethod
    def __init__(self, repository: AbstractExpenseRepository):
        raise NotImplementedError

    @abstractmethod
    def execute(self):
        raise NotImplementedError
