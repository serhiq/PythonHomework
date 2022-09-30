from unittest import TestCase

from main import power_numbers, ODD, filter_numbers, EVEN, PRIME


class TestHomeWork1(TestCase):

    def test_power_numbers(self):
        self.assertEqual(power_numbers(5), [25])

    def test_power_numbers_three_arg(self):
        self.assertEqual(power_numbers(1, 2, 0), [1, 4, 0])

    def test_filter_odd(self):
        self.assertEqual([3, 5], filter_numbers(filter_type=ODD, numbers=[3, 2, 5]))

    def test_filter_even(self):
        self.assertEqual([2, 4], filter_numbers(filter_type=EVEN, numbers=[3, 2, 5, 4]))

    def test_filter_prime(self):
        got = list(range(1, 55))
        self.assertEqual([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53], filter_numbers(filter_type=PRIME, numbers=got))
