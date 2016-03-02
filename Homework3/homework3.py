from math import pi

import numpy
from numpy import linspace
from numpy import random

from utils import signal_noise_ratio

sampling = 1000
time_slices = linspace(0, 1, sampling)
bits = 16


def sin():
    signal_frequency = 10
    numbers = numpy.sin(2 * pi * signal_frequency * time_slices)
    snr = signal_noise_ratio(numbers, bits)
    print "Results for sin function:"
    print "Theoretical signal-to-noise ratio = %s" % (bits * 6.02)
    print "Calculated signal-to-noise ratio = %s" % snr


def random_numbers():
    numbers = random.uniform(-1.0, 1.0, sampling)
    snr = signal_noise_ratio(numbers, bits)
    print "Results for random values:"
    print "Theoretical signal-to-noise ratio = %s" % (bits * 6.02)
    print "Calculated signal-to-noise ratio = %s" % snr


sin()
random_numbers()
