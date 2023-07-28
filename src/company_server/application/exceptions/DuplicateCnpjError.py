"""exceptions.py"""


class DuplicateCnpjError(Exception):
    def __init__(self, message="duplicate cnpj"):
        super().__init__(message)
