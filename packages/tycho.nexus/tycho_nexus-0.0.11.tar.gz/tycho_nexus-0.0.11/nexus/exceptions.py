"""

All exceptions in use by the package.

"""

# Base Exception


class NexusException(Exception):
    """Base exception, can be used to catch all package exception"""

    def __init__(self, message: str):
        super().__init__(message)


class APIException(NexusException):
    """Base exception to catch all Nexus API error responses"""

    def __init__(self, code: int, message: str):
        self.code = code
        self.message = message

        super().__init__(f"({code}) {message}")


# Exceptions


class InvalidRequest(APIException):
    """Exception raised when an invalid request is made."""

    def __init__(self, message: str):
        super().__init__(3001, message)


class InvalidAuthentication(APIException):
    """Exception [usually] raised when an invalid API key is used."""

    def __init__(self, message: str):
        super().__init__(3013, message)


class RateLimited(APIException):
    """Exception raised when (somehow) a rate limit is hit."""

    def __init__(self, message: str):
        super().__init__(3029, message)


class UnknownAccount(APIException):
    """Exception raised when an account was queried but not found."""

    def __init__(self, message: str):
        super().__init__(4002, message)


class UnknownDiscordUser(APIException):
    """Exception raised when a non-existing Discord user is used."""

    def __init__(self, message: str):
        super().__init__(6014, message)
