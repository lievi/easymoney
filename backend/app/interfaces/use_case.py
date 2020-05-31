# Verify if put it here
from abc import ABC, abstractmethod
from interfaces.repository import AbstractRepository


class AbstractUseCase(ABC):
    @abstractmethod
    def __init__(self, repository: AbstractRepository):
        raise NotImplementedError

    @abstractmethod
    def execute(self):
        raise NotImplementedError
