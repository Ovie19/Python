from unittest import TestCase
from temperature_converter import convert_temperature

class TemperatureConverterTest(TestCase):

    def test_that_convert_temperature_from_celcius_to_fahreinheit_and_higher_threshold_value_returns_heat_alert(self):
        celcius = 100
        threshold = 200

        expected = convert_temperature(celcius, threshold)
        actual = "Heat alert"
        self.assertEqual(actual, expected)

    def test_that_convert_temperature_from_celcius_to_fahreinheit_and_lower_threshold_value_returns_cold_advisory(self):
        celcius = 50
        threshold = 200

        expected = convert_temperature(celcius, threshold)
        actual = "Cold advisory"
        self.assertEqual(actual, expected)

    def test_that_convert_temperature_from_fahreinheit_to_celcius_and_higher_threshold_value_returns_heat_alert(self):
        fahreinheit = 800
        threshold = 200

        expected = convert_temperature(fahreinheit, threshold, "F")
        actual = "Heat alert"
        self.assertEqual(actual, expected)

    def test_that_convert_temperature_from_fahreinheit_to_celcius_and_lower_threshold_value_returns_cold_advisory(self):
        fahreinheit = 10
        threshold = 30

        expected = convert_temperature(fahreinheit, threshold, "F")
        actual = "Cold advisory"
        self.assertEqual(actual, expected)