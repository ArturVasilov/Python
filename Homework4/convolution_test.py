import unittest

from numba import int16
from numpy import random

from datetime import datetime

from convolution import direct_convolution
from convolution import fourier_convolution


def call_fourier(xs, ys):
    fourier = fourier_convolution(xs, ys)
    fourier_list = []
    for value in fourier:
        fourier_list.append(int16(round(abs(value))))
    return fourier_list


# noinspection PyArgumentList
class FourierConvolutionTest(unittest.TestCase):

    def test_direct_convolution(self):
        xs = [1, 3, 5]
        ys = [4, 2, 1]
        direct = direct_convolution(xs, ys)
        result = [17, 19, 27]
        self.assertListEqual(result, direct)

    def test_fourier_convolution(self):
        xs = [1, 3, 5]
        ys = [4, 2, 1]
        fourier = call_fourier(xs, ys)
        result = [17, 19, 27]
        self.assertListEqual(result, fourier)

    def test_small_fixed_input(self):
        xs = [1, 3, 7, 10, 54, 19, 8, 21]
        ys = [4, 71, 12, 23, 6, 9, 112, 48]
        direct = direct_convolution(xs, ys)
        fourier = call_fourier(xs, ys)
        self.assertListEqual(direct, fourier)

    def test_small_random_set(self):
        xs = int16(random.rand(10) * 50)
        ys = int16(random.rand(10) * 50)
        direct = direct_convolution(xs, ys)
        fourier = call_fourier(xs, ys)
        self.assertListEqual(direct, fourier)

    def test_large_random_set(self):
        xs = int16(random.rand(100) * 10)
        ys = int16(random.rand(100) * 10)
        direct = direct_convolution(xs, ys)
        fourier = call_fourier(xs, ys)
        self.assertListEqual(direct, fourier)

    def test_very_large_random(self):
        xs = int16(random.rand(1000) * 10)
        ys = int16(random.rand(1000) * 10)

        start = datetime.now()
        direct = direct_convolution(xs, ys)
        end = datetime.now()
        direct_time = end - start

        start = datetime.now()
        fourier = call_fourier(xs, ys)
        end = datetime.now()
        fourier_time = end - start

        self.assertListEqual(direct, fourier)
        self.assertTrue(fourier_time < direct_time / 10)


if __name__ == '__main__':
    unittest.main()
