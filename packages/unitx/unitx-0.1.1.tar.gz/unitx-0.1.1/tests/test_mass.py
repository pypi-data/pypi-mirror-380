"""Testing Library"""
import pytest
from unitx import Distance, Mass, convert_mass
from unitx import InvalidUnitError, NonNumericError, UnsupportedUnitError

def test_conversion():
    """Tests the conversion so its converting right."""

    converted = convert_mass(10, Mass.KILOGRAM, Mass.GRAM) # Metric Conversion
    assert converted == 10000

    converted = convert_mass(10, Mass.OUNCE, Mass.POUND) # Imperial Conversion
    assert round(converted, 3) == 0.625

    converted = convert_mass(10, Mass.TONNE, Mass.STONE) # Metric --> Imperial
    assert round(converted, 8) == 1574.73044418

def test_errors():
    """Tests the conversion errors so its been handled properly."""

    # Value is non numeric
    with pytest.raises(NonNumericError):
        convert_mass("string", Mass.OUNCE, Mass.POUND)

    # Unit is not enum
    with pytest.raises(UnsupportedUnitError):
        convert_mass(10, "non enum", Mass.KILOGRAM)

    with pytest.raises(UnsupportedUnitError):
        convert_mass(10, Mass.GRAM, "non enum")

    # Unit is category mismatch
    with pytest.raises(InvalidUnitError):
        convert_mass(10, Distance.FEET, Mass.POUND)

    with pytest.raises(InvalidUnitError):
        convert_mass(10, Mass.TONNE, Distance.YARDS)

    # Enum is from Mass class
    with pytest.raises(InvalidUnitError):
        convert_mass(10, Distance.CENTIMETERS, Distance.INCHES)
