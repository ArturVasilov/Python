from pylab import plot, figure, show

from numpy import pi, linspace, sin


def h_values(t_linspace, period):
    return sin(t_linspace * pi / period) / t_linspace * pi


def x_values(t_linspace, m_param):
    return sin(2 * pi * t_linspace * m_param)


def y_values(t_linspace, period, m_param, start, end):
    result = 0
    for index in range(start, end):
        result += x_values(index + t_linspace, m_param) * h_values(t_linspace - index * period, period)
    return period * result / 10

M = 3
T = 3
count = 100
t = linspace(-100, 100, count)

x = x_values(t, T)
figure("Sinus dots")
plot(t, x, 'r+')

figure("Sinus built")
plot(t[1:], y_values(t[1:], count * 100, M, -10, 10))
show()
