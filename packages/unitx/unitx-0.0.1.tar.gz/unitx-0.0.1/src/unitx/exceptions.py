"""Exceptions Module"""

class UnsupportedUnitError(Exception):
    """Raised when a unit is not recognized."""

    def __init__(self, message):
        super().__init__(message)

class InvalidUnitError(Exception):
    """Raised when units are from a different category."""

    def __init__(self, message):
        super().__init__(message)

class NonNumericError(Exception):
    """Raised when value is not int or float."""

    def __init__(self, message):
        super().__init__(message)
