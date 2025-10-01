"""Testing Library"""
import pytest
from unitx import Mass, Distance, convert_distance
from unitx import InvalidUnitError, NonNumericError, UnsupportedUnitError

def test_conversion():
    """Tests the conversion so its converting right."""

    converted = convert_distance(10, Distance.KILOMETERS, Distance.METERS) # Metric Conversion
    assert converted == 10000

    converted = convert_distance(10, Distance.FEET, Distance.INCHES) # Imperial Conversion
    assert converted == 120

    converted = convert_distance(10, Distance.METERS, Distance.MILES) # Metric --> Imperial
    assert round(converted, 8) == 0.00621373

def test_errors():
    """Tests the conversion errors so its been handled properly."""

    # Value is non numeric
    with pytest.raises(NonNumericError):
        convert_distance("string", Distance.FEET, Distance.YARDS)

    # Unit is not enum
    with pytest.raises(UnsupportedUnitError):
        convert_distance(10, "non enum", Distance.YARDS)

    with pytest.raises(UnsupportedUnitError):
        convert_distance(10, Distance.YARDS, "non enum")

    # Unit is category mismatch
    with pytest.raises(InvalidUnitError):
        convert_distance(10, Mass.KILOGRAM, Distance.YARDS)

    with pytest.raises(InvalidUnitError):
        convert_distance(10, Distance.FEET, Mass.MILLIGRAM)

    # Enum is from distance class
    with pytest.raises(InvalidUnitError):
        convert_distance(10, Mass.KILOGRAM, Mass.TONNE)
