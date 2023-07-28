"""paginate company errors"""


class DuplicateCnpjError(Exception):
    """duplicate company error"""

    def __init__(self, message="duplicate cnpj"):
        super().__init__(message)
