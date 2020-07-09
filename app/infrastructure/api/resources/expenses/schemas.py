from typing import Optional

from pydantic import BaseModel


class ExpenseBaseSchema(BaseModel):
    name: str
    description: Optional[str] = None
    value: float


class ExpenseSchema(ExpenseBaseSchema):
    id: int

    class Config:
        # This work with normal classes
        # TODO: Verify how to use them to use with the Entity
        orm_mode = True


class ExpenseCreateSchema(ExpenseBaseSchema):
    ...
