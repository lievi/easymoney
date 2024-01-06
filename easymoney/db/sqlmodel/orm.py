from sqlmodel import Field, SQLModel

from easymoney.domain.expense import ExpenseCreation


class ExpenseDB(SQLModel, ExpenseCreation, table=True):
    id: int | None = Field(default=None, primary_key=True)
