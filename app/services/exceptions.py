class ObjectNotFound(Exception):
    def __init__(self, detail=None) -> None:
        self.detail = detail or "Object not found"


class ExpenseNotFound(ObjectNotFound):
    def __init__(self) -> None:
        super().__init__("Expense not found")
