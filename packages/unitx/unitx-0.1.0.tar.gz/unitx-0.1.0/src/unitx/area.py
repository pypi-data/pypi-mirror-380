"""Converts units of area"""
from enum import Enum
from .validate import _validate_conversion

class Area(Enum):
    """Class for which contains Area Enums.

    Args:
        Enum (float): The Area Enum.
    """
    SQUARE_METER = 1.0
    SQUARE_KILOMETER = 1_000_000.0
    SQUARE_CENTIMETER = 0.0001
    SQUARE_MILLIMETER = 0.000001
    HECTARE = 10_000.0
    ACRE = 4046.86
    SQUARE_FOOT = 0.092903
    SQUARE_YARD = 0.836127
    SQUARE_MILE = 2_589_988.0

def convert_area(value: float, from_unit: Area, to_unit: Area)  -> float:
    """Convert a area value from a unit to another unit.

    Args:
        value (float): The numeric value to convert.
        from_unit (Area): The unit you are converting from.
        to_unit (Area): The unit you are converting to.

    Raises:
        NonNumericError: Raised when value is not int or float.
        UnsupportedUnitError: Raised when a unit is not recognized.
        InvalidUnitError: Raised when units are from a different category.

    Returns:
        float: The converted numeric value
    """

    _validate_conversion(value, from_unit, to_unit, Area)

    return value * from_unit.value / to_unit.value
