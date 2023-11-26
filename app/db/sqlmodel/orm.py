from sqlmodel import Field, SQLModel

from app.domain.expense import ExpenseCreation


class ExpenseDB(SQLModel, ExpenseCreation, table=True):
    id: int | None = Field(default=None, primary_key=True)
