from unittest import TestCase
from discount_calculator import get_discounted_price

class DiscountCalculatorTest(TestCase):

    def test_that_get_discounted_price_using_save10_promo_code_returns_ten_percent_discounted_price(self):
        item_name = "Play Station 5"
        item_price = 600000
        promo_code = "SAVE10"

        expected = get_discounted_price(item_name, item_price, promo_code)
        actual = 540000
        self.assertEqual(actual, expected)

    def test_that_get_discounted_price_using_half_off_promo_code_returns_fifty_percent_discounted_price(self):
        item_name = "Play Station 5"
        item_price = 600000
        promo_code = "HALFOFF"

        expected = get_discounted_price(item_name, item_price, promo_code)
        actual = 300000
        self.assertEqual(actual, expected)

    def test_that_get_discounted_price_using_invalid_promo_code_returns_item_price(self):
        item_name = "Play Station 5"
        item_price = 600000
        promo_code = "promo"

        expected = get_discounted_price(item_name, item_price, promo_code)
        actual = 600000
        self.assertEqual(actual, expected)