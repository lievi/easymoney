class RepositoryException(Exception):
    def __init__(
        self, message: str = "Unexpected error on repository"
    ) -> None:
        self.message = message

        super().__init__(self.message)

    def __str__(self) -> str:
        return self.message


class RepositoryTimeoutException(RepositoryException):
    def __init__(
        self, message: str = ("Timeout Error when accessing the repository")
    ) -> None:
        super().__init__(message)


class IdNotFoundException(RepositoryException):
    def __init__(self, message: str = "Id not found on expense") -> None:
        super().__init__(message)
