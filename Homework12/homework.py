from numpy import real, zeros
from numpy.core.umath import pi, exp
from pylab import show
from scipy.signal import hilbert

from signals.utils.utils import read_wav_file, draw_signal, write_wav_file

fr, dti = read_wav_file('D:\\voice.wav')

draw_signal(dti, fr / 2, 'Original signal')

h = hilbert(dti)
draw_signal(h, fr / 2, 'Hilbert signal')

w = 1000  # voice is still not very bad
w0 = 1.0 * w / fr
size = len(dti)
z = zeros(size)
for i in range(0, size):
    z[i] = h[i] * exp(2 * pi * 1j * w0 * i)
xs = real(z)
draw_signal(xs, fr / 2, 'Shifted signal')

write_wav_file('D:\\shifted_voice.wav', fr, xs)

show()
