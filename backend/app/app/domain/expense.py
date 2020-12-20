from typing import Optional

from pydantic import BaseModel

# TODO: Remove the pydantic


class ExpenseBase(BaseModel):
    name: str
    description: Optional[str] = None
    value: float


class ExpenseCreate(ExpenseBase):
    pass


class Expense(ExpenseBase):
    id: int

    class Config:
        orm_mode = True
