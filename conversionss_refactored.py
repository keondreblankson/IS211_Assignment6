class ConversionNotPossible(Exception):
    pass


def convert(fromUnit, toUnit, value):

    temperature_units = ["Celsius", "Fahrenheit", "Kelvin"]
    distance_units = ["Miles", "Yards", "Meters"]

    if fromUnit == toUnit:
        return float(value)

    # Temperature conversions
    if fromUnit in temperature_units and toUnit in temperature_units:

        # convert everything to Celsius first
        if fromUnit == "Celsius":
            celsius = value
        elif fromUnit == "Fahrenheit":
            celsius = (value - 32) * 5/9
        elif fromUnit == "Kelvin":
            celsius = value - 273.15

        # convert Celsius to target
        if toUnit == "Celsius":
            return celsius
        elif toUnit == "Fahrenheit":
            return (celsius * 9/5) + 32
        elif toUnit == "Kelvin":
            return celsius + 273.15

    # Distance conversions
    if fromUnit in distance_units and toUnit in distance_units:

        # convert to meters first
        if fromUnit == "Miles":
            meters = value * 1609.34
        elif fromUnit == "Yards":
            meters = value * 0.9144
        elif fromUnit == "Meters":
            meters = value

        # convert meters to target
        if toUnit == "Miles":
            return meters / 1609.34
        elif toUnit == "Yards":
            return meters / 0.9144
        elif toUnit == "Meters":
            return meters

    raise ConversionNotPossible("Cannot convert between these units")
