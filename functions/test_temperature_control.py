from unittest import TestCase
import temperature_control

class TestTemperatureControl(TestCase):
    
    def test_that_get_temp_advisory_control_function_exist(self):
        temperature_control.get_temp_advisory_control(50, 60, "C")

    def test_that_get_test_advisory_default_value_works(self):
        actual = temperature_control.get_temp_advisory_control(50, 60,)
        expected = 122, "cold advisory"
        self.assertEqual(actual, expected)

    def test_that_invalid_unit_raises_value_error(self):
        with self.assertRaises(ValueError):
            temperature_control.get_temp_advisory_control(50, 60, "W")

    def test_that_get_test_advisory_in_celsius_works(self):
        actual = temperature_control.get_temp_advisory_control(50, 60, "C")
        expected = 122, "cold advisory"
        self.assertEqual(actual, expected)

    def test_that_get_test_advisory_in_fahrenheit_works(self):
        actual = temperature_control.get_temp_advisory_control(158, 140, "F")
        expected = 70, "Heat alert"
        self.assertEqual(actual, expected)

    def test_that_get_test_advisory_default_value_works(self):
        actual = temperature_control.get_temp_advisory_control(50, 60,)
        expected = 122, "cold advisory"
        self.assertEqual(actual, expected)


