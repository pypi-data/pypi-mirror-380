"""Converts units of distances"""
from enum import Enum
from .validate import _validate_conversion

class Distance(Enum):
    """Class for which contains Distance Enums.

    Args:
        Enum (float): The Distance Enum.
    """
    METERS = 1.0
    KILOMETERS = 1000.0
    CENTIMETERS = 0.01
    MILLIMETERS = 0.001
    FEET = 0.3048
    INCHES = 0.0254
    YARDS = 0.9144
    MILES = 1609.34

def convert_distance(value: float, from_unit: Distance, to_unit: Distance)  -> float:
    """Convert a distance value from a unit to another unit.

    Args:
        value (float): The numeric value to convert.
        from_unit (Distance): The unit you are converting from.
        to_unit (Distance): The unit you are converting to.

    Raises:
        NonNumericError: Raised when value is not int or float.
        UnsupportedUnitError: Raised when a unit is not recognized.
        InvalidUnitError: Raised when units are from a different category.

    Returns:
        float: The converted numeric value
    """

    _validate_conversion(value, from_unit, to_unit, Distance)

    return value * from_unit.value / to_unit.value
