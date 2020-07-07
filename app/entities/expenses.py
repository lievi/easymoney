from dataclasses import dataclass, field
from typing import Optional, Dict


@dataclass(frozen=True)
class Expense:
    id: int = field(init=False)
    name: str
    value: float
    description: Optional[str] = None

    @classmethod
    def from_dict(cls, expense_dict: Dict):
        return cls(**expense_dict)
