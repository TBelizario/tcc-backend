# 404 exception for error handler
class NotFound(Exception):
    def __init__(self, name: str) -> None:
        self.name = name


# 422 exception for error handler
class UnprocessableEntity(Exception):
    def __init__(self, message: str) -> None:
        self.message = message


# 400 exception for error handler
class BadRequest(Exception):
    def __init__(self, message: str) -> None:
        self.message = message


# 401 exception for error handler
class NotAuthorized(Exception):
    def __init__(self, message: str) -> None:
        self.message = message


# 403 exception for error handler
class Forbidden(Exception):
    def __init__(self, message: str) -> None:
        self.message = message


# 500 exception for error handler
class ServerError(Exception):
    def __init__(self, message: str) -> None:
        self.message = message
