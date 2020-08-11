from sqlalchemy import Column, String, Float, Integer

from app.infrastructure.db.config.base_class import Base


class Expense(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    value = Column(Float)
