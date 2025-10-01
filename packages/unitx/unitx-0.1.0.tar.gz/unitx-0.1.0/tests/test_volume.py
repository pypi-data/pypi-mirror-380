"""Testing Library"""
import pytest
from unitx import Distance, Volume, convert_volume
from unitx import InvalidUnitError, NonNumericError, UnsupportedUnitError

def test_conversion():
    """Tests the conversion so its converting right."""

    converted = convert_volume(10, Volume.LITER, Volume.MILLILITER) # Metric Conversion
    assert converted == 10000

    converted = convert_volume(10, Volume.GALLON_US, Volume.PINT_US) # Imperial Conversion
    assert round(converted, 3) == 80

    converted = convert_volume(10, Volume.CUBIC_METER, Volume.PINT_US) # Metric --> Imperial
    assert converted == 21133.78531455526

def test_errors():
    """Tests the conversion errors so its been handled properly."""

    # Value is non numeric
    with pytest.raises(NonNumericError):
        convert_volume("string", Volume.GALLON_US, Volume.MILLILITER)

    # Unit is not enum
    with pytest.raises(UnsupportedUnitError):
        convert_volume(10, "non enum", Volume.PINT_US)

    with pytest.raises(UnsupportedUnitError):
        convert_volume(10, Volume.GALLON_US, "non enum")

    # Unit is category mismatch
    with pytest.raises(InvalidUnitError):
        convert_volume(10, Distance.FEET, Volume.CUBIC_METER)

    with pytest.raises(InvalidUnitError):
        convert_volume(10, Volume.PINT_US, Distance.YARDS)

    # Enum is from Volume class
    with pytest.raises(InvalidUnitError):
        convert_volume(10, Distance.CENTIMETERS, Distance.INCHES)
