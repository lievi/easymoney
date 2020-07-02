# TODO: Verify if make sense this base class stay here in the DB folder
from typing import Any

from sqlalchemy.ext.declarative import as_declarative, declared_attr


@as_declarative()
class Base:
    id: Any
    __name__: str
    # Generate the tablename based on the model class name
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()
