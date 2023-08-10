from typing import Optional

from pydantic import ConfigDict, BaseModel


class ExpenseBase(BaseModel):
    name: str
    description: Optional[str] = None
    value: float


class Expense(ExpenseBase):
    id: int
    model_config = ConfigDict(from_attributes=True)


class ExpenseCreate(ExpenseBase):
    pass
