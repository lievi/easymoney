from typing import Optional

from pydantic import BaseModel

# TODO: Remove the pydantic


class Expense(BaseModel):
    name: str
    description: Optional[str] = None
    value: float


class ExpenseInDb(Expense):
    id: int

    class Config:
        orm_mode = True
