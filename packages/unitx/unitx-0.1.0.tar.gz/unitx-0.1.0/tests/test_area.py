"""Testing Library"""
import pytest
from unitx import Mass, Area, convert_area
from unitx import InvalidUnitError, NonNumericError, UnsupportedUnitError

def test_conversion():
    """Tests the conversion so its converting right."""

    converted = convert_area(10, Area.SQUARE_KILOMETER, Area.SQUARE_METER) # Metric Conversion
    assert converted == 10_000_000

    converted = convert_area(10, Area.SQUARE_FOOT, Area.SQUARE_YARD) # Imperial Conversion
    assert converted == 10 / 9

    converted = convert_area(10, Area.SQUARE_METER, Area.SQUARE_MILE) # Metric --> Imperial
    assert round(converted, 8) == 3.86e-06

def test_errors():
    """Tests the conversion errors so its been handled properly."""

    # Value is non numeric
    with pytest.raises(NonNumericError):
        convert_area("string", Area.SQUARE_FOOT, Area.SQUARE_YARD)

    # Unit is not enum
    with pytest.raises(UnsupportedUnitError):
        convert_area(10, "non enum", Area.SQUARE_YARD)

    with pytest.raises(UnsupportedUnitError):
        convert_area(10, Area.SQUARE_YARD, "non enum")

    # Unit is category mismatch
    with pytest.raises(InvalidUnitError):
        convert_area(10, Mass.KILOGRAM, Area.SQUARE_YARD)

    with pytest.raises(InvalidUnitError):
        convert_area(10, Area.SQUARE_FOOT, Mass.MILLIGRAM)

    # Enum is from area class
    with pytest.raises(InvalidUnitError):
        convert_area(10, Mass.KILOGRAM, Mass.TONNE)
