class OpenCNPJError(Exception):
    """
    Generic erros of OpenCNPJ library
    """
    def __init__(self, message="An unexpected custom error occurred", error_code=None):
        super().__init__(message)
        self.message = message
        self.error_code = error_code

    def __str__(self):
        if self.error_code:
            return f"Error {self.error_code}: {self.message}"
        return self.message

class InvalidCNPJError(Exception):
    """
    Invalid CNPJ format error
    """
    def __init__(self, message="An unexpected custom error occurred", error_code=None):
        super().__init__(message)
        self.message = message
        self.error_code = error_code

    def __str__(self):
        if self.error_code:
            return f"Error {self.error_code}: {self.message}"
        return self.message
    
class CNPJNotFoundError(Exception):
    """
    CNPJ not found
    """
    def __init__(self, message="An unexpected custom error occurred", error_code=None):
        super().__init__(message)
        self.message = message
        self.error_code = error_code

    def __str__(self):
        if self.error_code:
            return f"Error {self.error_code}: {self.message}"
        return self.message