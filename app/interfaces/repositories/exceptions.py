class RepositoryException(Exception):
    def __init__(self, message="Unexpected error on repository") -> None:
        self.message = message

        super().__init__(self.message)
