from dataclasses import dataclass, field
from typing import Optional, Dict


@dataclass
class Expense:
    id: int = field(init=False, repr=False)
    name: str
    value: float
    description: Optional[str] = None

    @classmethod
    def from_dict(cls, expense_dict: Dict):
        return cls(**expense_dict)

    def to_dict(self) -> dict:
        return self.__dict__
