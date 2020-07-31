from typing import Optional

from pydantic import BaseModel


class ExpenseSchema(BaseModel):
    name: str
    description: Optional[str] = None
    value: float

    class Config:
        # Using this orm_mode, i can instantiate a new schema from an
        # entity, using the .from_orm
        orm_mode = True


class ExpenseOutputSchema(ExpenseSchema):
    id: int
