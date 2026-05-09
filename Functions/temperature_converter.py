def convert_temperature(temperature_value, threshold, unit="C"):
#    converted_temperature
    if unit.upper() == "F":
        converted_temperature = (temperature_value - 32) * 5 / 9
    else:
        converted_temperature = (temperature_value * 9 / 5) + 32

    if converted_temperature < threshold:
        return "Cold advisory"

    return "Heat alert"