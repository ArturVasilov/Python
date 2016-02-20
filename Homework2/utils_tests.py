import unittest

from utils import is_different_sign
from utils import zero_crossing_count
from utils import zero_crossing_counts_list


class DifferentSignTest(unittest.TestCase):

    def test_sign_both_positive(self):
        self.assertFalse(is_different_sign(1, 2))

    def test_sign_positive_negative(self):
        self.assertTrue(is_different_sign(1, -5))

    def test_sign_negative_positive(self):
        self.assertTrue(is_different_sign(-18, 91))

    def test_sign_negative_negative(self):
        self.assertFalse(is_different_sign(-100, -200))


class ZeroCrossingTest(unittest.TestCase):

    def test_zero_crossing_all_positive(self):
        numbers = [1, 2, 3, 4, 1, 5]
        self.assertEquals(0, zero_crossing_count(numbers))

    def test_zero_crossing_all_positive_one_zero(self):
        numbers = [1, 2, 3, 4, 0, 5]
        self.assertEquals(1, zero_crossing_count(numbers))

    def test_zero_crossing_two_zeros(self):
        numbers = [0, 0, 5]
        self.assertEquals(2, zero_crossing_count(numbers))

    def test_zero_crossing_one(self):
        numbers = [1, 2, 5, -1, -2]
        self.assertEquals(1, zero_crossing_count(numbers))

    def test_zero_crossing_three_times(self):
        numbers = [1, -1, 100, 20, 3, -5]
        self.assertEquals(3, zero_crossing_count(numbers))

    def test_zero_crossing_many_times(self):
        numbers = [1, -1, 1, -1, 1, -2, 2, -2, 3, -3, 5, -5, 1, 2, -6]
        self.assertEquals(13, zero_crossing_count(numbers))


class ZeroCrossingListTest(unittest.TestCase):

    def test_empty_list(self):
        numbers = []
        results = zero_crossing_counts_list(numbers, 0, 128)
        self.assertEquals(0, len(results))

    def test_full_overlay(self):
        numbers = [5, -5, 5, -5]
        self.assertRaises(Exception, zero_crossing_counts_list, numbers, 1, 2)

    def test_one_element(self):
        numbers = [5]
        results = zero_crossing_counts_list(numbers, 0.5, 2)
        self.assertEquals(1, len(results))
        self.assertEquals(0, results[0])

    def test_no_overlay(self):
        numbers = [5, 10, -10, 20, 15, 5, 3, -2, 8, -6]
        results = zero_crossing_counts_list(numbers, 0, 2)
        self.assertEquals([0, 1, 0, 1, 1], results)

    def test_no_overlay_not_same_size_of_parts(self):
        numbers = [5, 10, -10, 20, -5]
        results = zero_crossing_counts_list(numbers, 0, 2)
        self.assertEquals([0, 1, 0], results)

    def test_one_half_overlay(self):
        numbers = [4, -5, 2, -3, 5, 8, -30, 30]
        results = zero_crossing_counts_list(numbers, 0.5, 4)
        self.assertEquals([3, 2, 2, 1], results)

    def test_one_half_overlay_2(self):
        numbers = [1, -1, 1, -1, -3, -5, 5, 6, 8, -4, -6]
        results = zero_crossing_counts_list(numbers, 0.5, 4)
        self.assertEquals([3, 1, 1, 1, 1, 0], results)

if __name__ == '__main__':
    unittest.main()
