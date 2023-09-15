from typing import Any, Generic, Optional, Type, TypeVar

from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from sqlalchemy.orm import Session

from .orm.base import BaseOrm

# Create a generic model that can be any model based on the `Base` class
ModelType = TypeVar('ModelType', bound=BaseOrm)
CreateModelType = TypeVar('CreateModelType', bound=BaseModel)


class CRUDBase(Generic[ModelType, CreateModelType]):
    def __init__(self, model: Type[ModelType], db: Session):
        """CRUD methods to generics Models based on the `base_class`
        This is a base implementation for the repositories, that do a base
        CRUD on the database

        Arguments:
            model {Type[ModelType]} -- A SQLAlchemy model class
        """
        self.model: BaseOrm = model
        self.db = db

    def get(self, id: Any) -> Optional[ModelType]:
        return self.db.query(self.model).filter(self.model.id == id).first()

    def create(self, obj_in: CreateModelType) -> ModelType:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)
        self.db.add(db_obj)
        return db_obj
