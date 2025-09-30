"""Converts units of mass"""
from enum import Enum
from .validate import _validate_conversion

class Mass(Enum):
    """Class for which contains Mass Enums.

    Args:
        Enum (float): The Mass Enum.
    """
    KILOGRAM = 1.0
    GRAM = 0.001
    MILLIGRAM = 0.000001
    MICROGRAM = 1e-9
    TONNE = 1000.0
    POUND = 0.45359237
    OUNCE = 0.0283495231
    STONE = 6.35029318

def convert_mass(value: float, from_unit: Mass, to_unit: Mass)  -> float:
    """Convert a mass value from a unit to another unit.

    Args:
        value (float): The numeric value to convert.
        from_unit (Mass): The unit you are converting from.
        to_unit (Mass): The unit you are converting to.

    Raises:
        NonNumericError: Raised when value is not int or float.
        UnsupportedUnitError: Raised when a unit is not recognized.
        InvalidUnitError: Raised when units are from a different category.

    Returns:
        float: The converted numeric value
    """

    _validate_conversion(value, from_unit, to_unit, Mass)

    return value * from_unit.value / to_unit.value
