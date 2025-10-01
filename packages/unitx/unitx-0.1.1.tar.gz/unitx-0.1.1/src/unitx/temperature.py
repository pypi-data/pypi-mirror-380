"""Converts units of temperature"""
from enum import Enum
from .validate import _validate_conversion

class Temperature(Enum):
    """Class for which contains Temperature Enums.

    Args:
        Enum (float): The Temperature Enum.
    """
    CELSIUS = "C"
    FAHRENHEIT = "F"
    KELVIN = "K"
    RANKINE = "R"

def convert_temperature(value: float, from_unit: Temperature, to_unit: Temperature) -> float:
    """Convert a temperature value from a unit to another unit.

    Args:
        value (float): The numeric value to convert.
        from_unit (Temperature): The unit you are converting from.
        to_unit (Temperature): The unit you are converting to.

    Raises:
        NonNumericError: Raised when value is not int or float.
        UnsupportedUnitError: Raised when a unit is not recognized.
        InvalidUnitError: Raised when units are from a different category.

    Returns:
        float: The converted numeric value
    """

    _validate_conversion(value, from_unit, to_unit, Temperature)

    converted_value = None

    if from_unit == Temperature.CELSIUS:
        converted_value = value
    elif from_unit == Temperature.FAHRENHEIT:
        converted_value = (value - 32) * 5/9
    elif from_unit == Temperature.KELVIN:
        converted_value = value - 273.15
    elif from_unit == Temperature.RANKINE:
        converted_value = (value - 491.67) * 5/9

    # Convert from Celsius to target unit
    if to_unit == Temperature.FAHRENHEIT:
        converted_value = converted_value * 9/5 + 32
    elif to_unit == Temperature.KELVIN:
        converted_value = converted_value + 273.15
    elif to_unit == Temperature.RANKINE:
        converted_value = (converted_value + 273.15) * 9/5

    return converted_value
