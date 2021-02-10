class ObjectNotFound(Exception):
    def __init__(self, detail: str = None) -> None:
        self.detail = detail or 'Object not found'


class ExpenseNotFound(ObjectNotFound):
    def __init__(self, detail: str = None) -> None:
        self.detail = detail or 'Expense not found'
