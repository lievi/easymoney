from typing import Optional

from pydantic import BaseModel


class ExpenseBase(BaseModel):
    name: str
    description: Optional[str] = None
    value: float


class Expense(ExpenseBase):
    id: int

    class Config:
        # This work with normal classes
        # TODO: Verify how to use them
        orm_mode = True


class ExpenseCreate(ExpenseBase):
    ...
