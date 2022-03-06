from fastapi import HTTPException


class ObjectNotFound(HTTPException):
    def __init__(self) -> None:
        self.status_code = 404
        self.detail = 'Item not found'