from abc import ABC, abstractmethod


class AbstractExpenseRepository(ABC):
    @abstractmethod
    def get_expense_by_id(self, id):
        raise NotImplementedError

    @abstractmethod
    def create_expense(self, expense):
        raise NotImplementedError
