from typing import Optional

from pydantic import BaseModel
from sqlmodel import Field, SQLModel


class ExpenseBase(BaseModel):
    name: str
    description: Optional[str] = None
    value: float


class ExpenseCreate(ExpenseBase):
    pass


class Expense(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    description: Optional[str] = None
    value: float