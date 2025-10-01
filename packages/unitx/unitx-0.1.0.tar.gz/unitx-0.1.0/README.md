# unitx
[![version](https://img.shields.io/pypi/v/unitx.svg?colorB=blue)](https://pypi.org/project/unitx/)
[![pyversions](https://img.shields.io/pypi/pyversions/unitx.svg?)](https://pypi.org/project/unitx/)
[![codecov](https://codecov.io/gh/devs-des1re/unitx/branch/main/graph/badge.svg?token=YOUR_CODECOV_TOKEN)](https://codecov.io/gh/devs-des1re/unitx)

A Python library which dynamically converts different types of units.

# Installation
To install unitx you will need `Python >= 3.10`

Run:
```
pip install unitx
```

Or:
```
python -m pip install unitx
```

Also works for MacOS and Linux with `pip3`.

# Conversions
There are different functions in unitx which help convert for you!

## Converting Distance
To convert distance, you'll use the `convert_distance` function. This also needs to be used with the enum class `Distance`.

```py
from unitx import convert_distance, Distance

converted_value = convert_distance(5, Distance.MILES, Distance.KILOMETERS)
print(converted_value)
```

## Converting Mass
To convert mass, you'll use the `convert_mass` function. This also needs to be used with the enum class `Mass`.

```py
from unitx import convert_mass, Mass

converted_value = convert_mass(1000, Mass.KILOGRAMS, Mass.TONNE)
print(converted_value)
```

## Converting Volume
To convert volume, you'll use the `convert_volume` function. This also needs to be used with the enum class `Volume`.

```py
from unitx import convert_volume, Volume

converted_value = convert_volume(10, Volume.LITER, Volume.MILLILITER)
print(converted_value)
```

## Converting Temperature
To convert temperature, you'll use the `convert_temperature` function. This also needs to be used with the enum class `Temperature`. 

**Note:** Units `kelvin` and `rankine` can also be converted

```py
from unitx import convert_temperature, Temperature

convert_temperature(0, Temperature.CELSIUS, Temperature.FAHRENHEIT)
print(converted_value)
```

## Converting Area
To convert area, you'll use the `convert_area` function. This also needs to be used with the enum class `Area`.

```py
from unitx import convert_Area, area

converted_value = convert_area(10, Area.SQUARE_KILOMETER, Area.SQUARE_METER)
print(converted_value)
```

# Enums
What are `enums`? `Enums` in Python are a way to define a set of symbolic names (constants) that are bound to unique, constant values. They make code more readable and organized by grouping related values under one type, instead of using plain integers or strings.

In Python, `enums` are created using the Enum class from the built-in enum module. Each member of an enum has a name and a value.

## Distance
Enum `Distance` contains float values for dynamic conversion, which just makes it simple for you to convert quickly and efficiently.

```py
from unitx import Distance

print(Distance.METERS)
print(Distance.KILOMETERS)
print(Distance.CENTIMETERS)
print(Distance.MILLIMETERS)
print(Distance.FEET)
print(Distance.INCHES)
print(Distance.YARDS)
print(Distance.MILES)
```

## Mass
Enum `Mass` contains float values for dynamic conversion, which just makes it simple for you to convert quickly and efficiently.

```py
from unitx import Mass

print(Mass.KILOGRAM)
print(Mass.GRAM)
print(Mass.MILLIGRAM)
print(Mass.MICROGRAM)
print(Mass.TONNE)
print(Mass.POUND)
print(Mass.OUNCE)
print(Mass.STONE)
```

## Temperature
Enum `Temperature` is a bit different. It contains a abbreviation, and then converts between the 4 of them .

```py
from unitx import Temperature

print(Temperature.CELSIUS)
print(Temperature.FAHRENHEIT)
print(Temperature.KELVIN)
print(Temperature.RANKINE)
```

## Volume
Enum `Volume` contains float values for dynamic conversion, which just makes it simple for you to convert quickly and efficiently.

```py
from unitx import Volume

print(Volume.LITER)
print(Volume.MILLILITER)
print(Volume.CUBIC_METER)
print(Volume.CUBIC_CENTIMETER)
print(Volume.GALLON_US)
print(Volume.QUART_US)
print(Volume.PINT_US)
print(Volume.CUP_US)
print(Volume.FLUID_OUNCE_US)
print(Volume.TABLESPOON_US)
print(Volume.TEASPOON_US)
```

## Area
Enum `Volume` contains float values for dynamic conversion, which just makes it simple for you to convert quickly and efficiently.

```py
from unitx import Area

print(Area.SQUARE_METER)
print(Area.SQUARE_KILOMETER)
print(Area.SQUARE_CENTIMETER)
print(Area.SQUARE_MILLIMETER)
print(Area.HECTARE)
print(Area.ACRE)
print(Area.SQUARE_FOOT)
print(Area.SQUARE_YARD)
print(Area.SQUARE_MILE)
```

# Exceptions
In programming, an exception is an event that occurs during the execution of a program that disrupts the normal flow of instructions. It usually happens when something goes wrong, like trying to divide by zero, accessing a file that doesn’t exist, or referencing a variable that hasn’t been defined. In `unitx` case, it tells you if you have passed invalid values for which then its raised.

## Unsupported Unit
This is raised when you have passed a unsupported value, even when passed from another enum! This is so that you are not passing random params.

```py
class UnsupportedUnitError(Exception):
    """Raised when a unit is not recognized."""

    def __init__(self, message):
        super().__init__(message)
```

## Invalid Unit
This is raised when you pass a enum from a different category which is not related to the conversion. This is so that you are converting properly.

```py
class InvalidUnitError(Exception):
    """Raised when units are from a different category."""

    def __init__(self, message):
        super().__init__(message)
```

## Non Numeric
This is raised when `value` is not a `int`/`float` object, and is something else, e.g. `str`, `list`, `dict`. This keeps the conversion easy and not full on annoying errors!

```py
class NonNumericError(Exception):
    """Raised when value is not int or float."""

    def __init__(self, message):
        super().__init__(message)
```

# Contributing
Contributions to this project are welcome! You can help by:

- Reporting bugs or issues

- Suggesting new features

- Writing or improving documentation

- Submitting code improvements or fixes

- Adding tests

## Note
Please check if another user has already said what you thought. It helps prevent repeating the same content, keeps conversations organized, and makes it easier to follow discussions. By using this, you can ensure that ideas stay unique, reduce clutter in busy channels, and maintain clarity in group chats or collaborative projects.