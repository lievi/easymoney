from dataclasses import dataclass
from typing import Optional, Dict


@dataclass(frozen=True)
class Expense:
    name: str
    value: float
    description: Optional[str] = None

    @classmethod
    def from_dict(cls, expense_dict: Dict):
        return cls(**expense_dict)
