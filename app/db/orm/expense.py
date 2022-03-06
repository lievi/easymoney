from sqlalchemy import Column, String, Float, Integer

from app.db.orm.base import BaseOrm


class Expense(BaseOrm):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    value = Column(Float)
