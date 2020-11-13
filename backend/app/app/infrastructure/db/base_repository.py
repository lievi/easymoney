from typing import Any, Generic, Optional, Type, TypeVar

from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.infrastructure.db.models.base import Base
from app.infrastructure.db.session import get_session, SessionLocal

# Create a generic model that can be any model based on the `Base` class
ModelType = TypeVar('ModelType', bound=Base)
CreateModelType = TypeVar('CreateModelType', bound=BaseModel)


class CRUDBase(Generic[ModelType, CreateModelType]):
    def __init__(self, model: Type[ModelType]):
        """CRUD methods to generics Models based on the `base_class`

        Arguments:
            model {Type[ModelType]} -- A SQLAlchemy model class
        """
        self.model: Base = model
        self.db: Session = get_session()
    def get(self, id: Any) -> Optional[ModelType]:
        print(dir(self.db))
        return self.db.query(self.model).filter(self.model.id == id).first()

    def create(self, *, obj_in: CreateModelType) -> ModelType:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj
