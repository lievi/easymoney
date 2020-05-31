from typing import Optional


class Expense():
    id: str
    name: str
    description: Optional[str] = None
    value: float
