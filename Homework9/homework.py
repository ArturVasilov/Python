from math import pi

from numpy import unwrap, angle, diff, linspace
from pylab import plot, figure, show
from scipy.signal import iirfilter, freqz, chirp, lfilter

order = 13
freq = 0.8

b, a = iirfilter(order, freq, btype='lowpass')
w, h = freqz(b, a)

figure("Filter")
plot(w / pi, abs(h))

figure("Filter phase delay")
hn = h / (abs(h))
plot(w, unwrap(angle(hn)))
plot(w, unwrap(angle(hn)) / w)

hn = h / (abs(h))
ha = angle(hn)
gd = diff(ha) / diff(w)
figure("Filter group delay")
plot(w[:-1], gd)

t = linspace(0, 1, 1000)
signal_chirp = chirp(t, f0=12.5, f1=2.5, t1=1, method='linear')
figure("Chirp linear signal before filters")
plot(t, signal_chirp)

signal_filtered = lfilter(b, a, signal_chirp)
figure("Chirp linear signal after filter")
plot(t, signal_filtered)

show()
