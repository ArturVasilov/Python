import struct
import wave

from numpy import linspace
from numpy.fft import fft
from scipy.io.wavfile import read
from pylab import plot, figure


def read_wav_file(name):
    wav_file = open(name, 'rb')
    [fr, dti] = read(wav_file)
    wav_file.close()
    return fr, dti


def write_wav_file(name, freq, values):
    wav_file = wave.open(name, 'wb')
    pck = []
    for value in values:
        pck.append(struct.pack('h', value))

    str_out = ''.join(pck)

    wav_file.setparams((1, 2, freq, 0, 'NONE', 'not compressed'))
    wav_file.writeframes(str_out)
    wav_file.close()


def draw_signal(signal, max_value, figure_name):
    fourier_signal = abs(fft(signal))
    figure(figure_name)
    t = linspace(0, max_value, len(fourier_signal) / 2)
    plot(t, fourier_signal[0:len(fourier_signal) / 2])
