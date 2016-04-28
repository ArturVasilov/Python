from math import pi

from numpy import sin, cos, linspace, imag, zeros, gradient
from numpy.core.umath import sign
from numpy.fft import fft
from numpy.ma import sqrt, arctan
from pylab import plot, figure, show
from scipy.signal import hilbert


def phase(signal, ort_signal):
    # prevent from division by zero
    count = len(signal)
    result = zeros(count)
    for i in range(0, count):
        if signal[i] == 0:
            result[i] = (pi / 2) * sign(ort_signal[i])
        else:
            result[i] = arctan(ort_signal[i] / signal[i])
    return result


a_0 = 1
m = 2
omega = 5
omega_0 = 100

size = 1000
t = linspace(0, 1, size)

s = a_0 * (1 + m * cos(omega * t)) * sin(omega_0 * t)

z = hilbert(s)
s_ort = imag(z)

a_signal = sqrt(s ** 2 + s_ort ** 2)
fi = phase(s_ort, s)

# I don't perfectly sure, that it's correct way for derivative, but let it be so
w = gradient(fi)

figure("Original signal")
plot(s)

figure("Original signal spectrum")
s_f = abs(fft(s))
plot(s_f)

figure("After Hilbert filter spectrum")
z_f = abs(fft(z))
plot(z_f)

figure("Amplitude")
plot(a_signal)

figure("Phase")
plot(fi)

figure("Instant frequency")
plot(w)

show()
