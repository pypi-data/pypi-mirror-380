"""Validates conversion"""
from enum import Enum
from .exceptions import InvalidUnitError, NonNumericError, UnsupportedUnitError


def _validate_conversion(value, from_unit, to_unit, category):
    # Check if value is numeric
    if not isinstance(value, (int, float)):
        raise NonNumericError(f"Value must be numeric, got {type(value).__name__}")

    # Check if units are valid Enum members
    if not isinstance(from_unit, Enum):
        raise UnsupportedUnitError(f"From unit must be enum, got {type(from_unit).__name__}")

    if not isinstance(to_unit, Enum):
        raise UnsupportedUnitError(f"From unit must be enum, got {type(to_unit).__name__}")

    # Check if category mismatch
    if from_unit.__class__ is not to_unit.__class__:
        raise InvalidUnitError(f"From unit and to unit must be from the category, got {type(from_unit).__name__}, {type(from_unit).__name__}")

    # Check if from unit is from correct category Enum
    if not isinstance(from_unit, category):
        raise InvalidUnitError(f"From unit must be from the {category.__name__} enum, got {type(from_unit).__name__}")
