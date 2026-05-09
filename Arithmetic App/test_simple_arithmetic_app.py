from unittest import TestCase
from simple_arithmetic_app import get_random_number

class SimpleArithmeticAppTest(TestCase):

    def test_that_get_random_number_returns_number_greater_than_zero(self):
        expected = get_random_number()
        self.assertTrue(expected > 0)