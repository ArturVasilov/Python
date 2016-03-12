from numpy import argmax
from numpy import diag, zeros, ones, vstack, hstack, dot
from numpy import correlate

from pylab import plot
from pylab import figure

import scipy.io.wavfile as sw


def generate_matrix(polynom):
    n = len(polynom)
    ones_diagonal = diag(ones(n - 1))
    zeros_vector = zeros((n - 1, 1))
    concat = hstack((zeros_vector, ones_diagonal))
    return vstack((concat, polynom))


def generate_s_vector(polynom):
    m = len(polynom)
    s = zeros(m)
    s[m - 1] = 1
    return s


def generate_watermark(polynom):
    m = len(polynom)
    s = generate_s_vector(polynom)
    matrix = generate_matrix(polynom)
    watermark = []
    for i in range(0, 2 ** m - 1):
        wk = dot(polynom, s) % 2
        wk = -1 if wk == 0 else 1
        watermark.append(wk)
        s = dot(matrix, s) % 2
    return watermark


def find_watermark_position(filename, polynom, draw):
    f = open(filename, 'rb')
    # noinspection PyUnusedLocal
    [fr, dti] = sw.read(f)
    f.close()

    w = generate_watermark(polynom)
    c = correlate(w, dti, 'full')

    if draw:
        figure()
        plot(c)

    return argmax(c)

# 471118
print find_watermark_position('watermark.wav', [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0], True)
