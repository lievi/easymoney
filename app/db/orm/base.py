# TODO: Verify if make sense this base class stay here in the DB folder
from typing import Any

from sqlalchemy.orm import as_declarative, declared_attr


@as_declarative()
class BaseOrm:
    id: Any
    __name__: str

    # Generate the tablename based on the model class name
    @declared_attr.directive
    def __tablename__(cls) -> str:
        return cls.__name__.lower()
