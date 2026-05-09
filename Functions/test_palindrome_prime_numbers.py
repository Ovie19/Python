from unittest import TestCase
from palindrome_prime_numbers import check_palindrome_and_prime

class PalindromePrimeNumbersTest(TestCase):

    def test_that_if_number_is_prime_and_not_palindrome_it_returns_false(self):

        number = 1033
        self.assertFalse(check_palindrome_and_prime(number))


    def test_that_if_number_is_not_prime_and_is_palindrome_it_returns_false(self):

        number = 3113
        self.assertFalse(check_palindrome_and_prime(number))

    def test_that_if_number_is_prime_and_palindrome_it_returns_true(self):

        number = 919
        self.assertTrue(check_palindrome_and_prime(number))

        number = 2
        self.assertTrue(check_palindrome_and_prime(number))

        number = 3
        self.assertTrue(check_palindrome_and_prime(number))