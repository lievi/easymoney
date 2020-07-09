from dataclasses import dataclass, field
from typing import Optional, Dict


@dataclass(frozen=True)
class Expense:
    # FIXME: Verify how to fix that
    # id: int = field(init=False)
    id: int
    name: str
    value: float
    description: Optional[str] = None

    @classmethod
    def from_dict(cls, expense_dict: Dict):
        return cls(**expense_dict)
