from typing import Optional


class Expense:
    def __init__(
        self,
        name: str,
        value: float,
        description: Optional[str] = None,
    ):
        self.name = name,
        self.value = value,
        self.description = description
