"""Converts units of volume"""
from enum import Enum
from .validate import _validate_conversion

class Volume(Enum):
    """Class for which contains Volume Enums.

    Args:
        Enum (float): The Volume Enum.
    """
    LITER = 1.0
    MILLILITER = 0.001
    CUBIC_METER = 1000.0
    CUBIC_CENTIMETER = 0.001
    GALLON_US = 3.78541
    QUART_US = 0.946353
    PINT_US = 0.473176
    CUP_US = 0.24
    FLUID_OUNCE_US = 0.0295735
    TABLESPOON_US = 0.0147868
    TEASPOON_US = 0.00492892

def convert_volume(value: float, from_unit: Volume, to_unit: Volume)  -> float:
    """Convert a volume value from a unit to another unit.

    Args:
        value (float): The numeric value to convert.
        from_unit (Volume): The unit you are converting from.
        to_unit (Volume): The unit you are converting to.

    Raises:
        NonNumericError: Raised when value is not int or float.
        UnsupportedUnitError: Raised when a unit is not recognized.
        InvalidUnitError: Raised when units are from a different category.

    Returns:
        float: The converted numeric value
    """

    _validate_conversion(value, from_unit, to_unit, Volume)

    return value * from_unit.value / to_unit.value
