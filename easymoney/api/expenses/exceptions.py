from typing import Any

from fastapi.exceptions import HTTPException
from pydantic import BaseModel


class HTTPErrorModel(BaseModel):
    detail: str


class BaseHTTPException(HTTPException):
    def __init__(
        self,
        status_code: int,
        detail: Any = None,
        headers: dict[str, str] | None = None,
    ) -> None:
        super().__init__(status_code, detail, headers)

    def open_api_doc(self, description=None) -> dict:
        return {
            "model": HTTPErrorModel,
            "description": description or None,
            "content": {
                "application/json": {
                    "example": HTTPErrorModel(detail=self.detail)
                }
            },
        }


class ItemNotFound(BaseHTTPException):
    def __init__(self, detail=None) -> None:
        detail = detail or "Item not found"
        super().__init__(status_code=404, detail=detail)
