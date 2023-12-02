from pydantic import BaseModel, validator



class BaseExpense(BaseModel):
    name: str
    description: str | None
    value: float


class Expense(BaseExpense):
    id: int


class ExpenseCreation(BaseExpense):
    pass


# TODO: put this on the schema
class ExpenseUpdate(BaseExpense):
    name: str | None
    value: float | None

    @validator("name", "value")
    def check_not_none(cls, v):
        """If an optional parameter is present, it should not be None"""
        assert v is not None, "The value should not be None"
        return v
