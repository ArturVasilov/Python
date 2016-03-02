import unittest
from math import pi

from numpy import linspace
from numpy.ma import sin
from numpy import random

from signals.lesson3.utils import signal_noise_ratio


class SignalToNoiseRatioTest(unittest.TestCase):

    sampling = 1000
    time_slices = linspace(0, 1, sampling)
    bits = 16

    def test_sinus_results_looks_like_correct(self):
        signal_frequency = 10
        numbers = sin(2 * pi * signal_frequency * self.time_slices)
        snr = signal_noise_ratio(numbers, self.bits)

        self.assertTrue(abs(96.32 - snr) < 2)

    def test_random_results_looks_like_correct(self):
        numbers = random.uniform(-1.0, 1.0, self.sampling)
        snr = signal_noise_ratio(numbers, self.bits)

        self.assertTrue(abs(96.32 - snr) < 2)

if __name__ == '__main__':
    unittest.main()