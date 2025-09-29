"""Tomling exceptions module"""

class DuplicateKeysError(Exception):
    """Exception raised when duplicate keys are found

    Args:
        message (str): The explanation of the error
    """
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class InvalidTomlError(Exception):
    """Exception raised when invalid toml values are found

    Args:
        message (str): The explanation of the error
    """
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class InvalidDictError(Exception):
    """Exception raised when invalid toml values are found

    Args:
        message (str): The explanation of the error
    """
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
