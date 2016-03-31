import numpy
from pylab import plot, figure, show

from numpy import pi, linspace, sin


def h_values(t_linspace, period):
    h = []
    for t_i in t_linspace:
        h.append((1.0 / period) if t_i == 0
                 else sin(t_i * pi / period) / (t_i * pi))
    return h


def x_values(t_linspace, m_param):
    return sin(2 * pi * t_linspace * m_param)


def y_values(t_linspace, period, x_items):
    result = []
    freq_sample = 10 * 1.0 / period
    time_linspace = linspace(0, 1, freq_sample)
    for t_i in time_linspace:
        h = h_values(t_i - t_linspace, period)
        result.append(numpy.sum(x_items * h) * period)
    return time_linspace, result


M = 10
f_sample = 13 * M
t = linspace(0, 1, f_sample)

x = x_values(t, M)
figure("Sinus dots")
plot(t, x, 'r+')

figure("Sinus built")
t_y, y = y_values(t, 1.0 / f_sample, x)
plot(t_y, y)
show()
