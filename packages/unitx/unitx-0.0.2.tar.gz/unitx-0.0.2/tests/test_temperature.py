"""Testing Library"""
import pytest
from unitx import Distance, Temperature, convert_temperature
from unitx import InvalidUnitError, NonNumericError, UnsupportedUnitError

def test_conversion():
    """Tests the conversion so its converting right."""

    converted = convert_temperature(10, Temperature.CELSIUS, Temperature.KELVIN) # Metric Conversion
    assert converted == 283.15

    converted = convert_temperature(32, Temperature.FAHRENHEIT, Temperature.RANKINE) # Imperial Conversion
    assert round(converted, 3) == 491.67

    converted = convert_temperature(0, Temperature.CELSIUS, Temperature.FAHRENHEIT) # Metric --> Imperial
    assert converted == 32

    converted = convert_temperature(10, Temperature.KELVIN, Temperature.CELSIUS) # codecov
    assert converted == -263.15

    converted = convert_temperature(10, Temperature.RANKINE, Temperature.FAHRENHEIT) # codecov
    assert round(converted, 5) == -449.67

def test_errors():
    """Tests the conversion errors so its been handled properly."""

    # Value is non numeric
    with pytest.raises(NonNumericError):
        convert_temperature("string", Temperature.CELSIUS, Temperature.FAHRENHEIT)

    # Unit is not enum
    with pytest.raises(UnsupportedUnitError):
        convert_temperature(10, "non enum", Temperature.CELSIUS)

    with pytest.raises(UnsupportedUnitError):
        convert_temperature(10, Temperature.RANKINE, "non enum")

    # Unit is category mismatch
    with pytest.raises(InvalidUnitError):
        convert_temperature(10, Distance.FEET, Temperature.CELSIUS)

    with pytest.raises(InvalidUnitError):
        convert_temperature(10, Temperature.RANKINE, Distance.YARDS)

    # Enum is from Temperature class
    with pytest.raises(InvalidUnitError):
        convert_temperature(10, Distance.CENTIMETERS, Distance.INCHES)
