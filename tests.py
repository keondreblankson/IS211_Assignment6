import conversions
import conversions_refactored


def test_celsius_to_kelvin():
    print("Testing Celsius to Kelvin")

    tests = [
        (0, 273.15),
        (100, 373.15),
        (300, 573.15),
        (-273.15, 0),
        (25, 298.15)
    ]

    for c, expected in tests:
        result = conversions.convertCelsiusToKelvin(c)
        print(f"{c}C -> Expected {expected}, Got {result}")
        assert round(result, 2) == round(expected, 2)


def test_celsius_to_fahrenheit():
    print("Testing Celsius to Fahrenheit")

    tests = [
        (0, 32),
        (100, 212),
        (300, 572),
        (-40, -40),
        (25, 77)
    ]

    for c, expected in tests:
        result = conversions.convertCelsiusToFahrenheit(c)
        print(f"{c}C -> Expected {expected}, Got {result}")
        assert round(result, 2) == round(expected, 2)


def test_refactored_temperature():
    print("Testing Refactored Temperature Conversions")

    assert round(conversions_refactored.convert("Celsius", "Kelvin", 0),2) == 273.15
    assert round(conversions_refactored.convert("Celsius", "Fahrenheit", 100),2) == 212
    assert round(conversions_refactored.convert("Kelvin", "Celsius", 273.15),2) == 0
    assert round(conversions_refactored.convert("Fahrenheit", "Celsius", 32),2) == 0


def test_refactored_distance():
    print("Testing Distance Conversions")

    assert round(conversions_refactored.convert("Miles","Meters",1),2) == 1609.34
    assert round(conversions_refactored.convert("Yards","Meters",1),2) == 0.91
    assert round(conversions_refactored.convert("Meters","Yards",1),2) == 1.09
    assert round(conversions_refactored.convert("Miles","Yards",1),2) == 1760


def test_same_unit():
    print("Testing Same Unit Conversion")

    assert conversions_refactored.convert("Celsius","Celsius",10) == 10
    assert conversions_refactored.convert("Miles","Miles",5) == 5


def test_invalid_conversion():
    print("Testing Invalid Conversion")

    try:
        conversions_refactored.convert("Celsius","Miles",100)
    except conversions_refactored.ConversionNotPossible:
        print("Correctly caught invalid conversion")


if __name__ == "__main__":
    test_celsius_to_kelvin()
    test_celsius_to_fahrenheit()
    test_refactored_temperature()
    test_refactored_distance()
    test_same_unit()
    test_invalid_conversion()

    print("All tests completed")
