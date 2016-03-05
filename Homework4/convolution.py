from numpy.fft import fft
from numpy.fft import ifft


def direct_convolution(xs, ys):
    n = len(xs)
    hs = []
    for i in range(0, n):
        value = 0
        for k in range(0, n):
            value += xs[i - k] * ys[k]
        hs.append(value)
    return hs


def fourier_convolution(xs, ys):
    x_fourier = fft(xs)
    y_fourier = fft(ys)
    h_fourier = x_fourier * y_fourier
    hs = ifft(h_fourier)
    return hs
