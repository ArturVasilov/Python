from math import sqrt

from numpy import pi, linspace, sin, var, correlate
from numpy.fft import fft
from pylab import plot, figure, show
from scipy.io.wavfile import read
from scipy.signal import firwin, filtfilt


def read_file():
    name = 'D:\\voice.wav'
    f = open(name, 'rb')
    [fr_read, dti_read] = read(f)
    f.close()
    dti_read = dti_read[:, 0]
    return fr_read, dti_read


def signal(sample_freq, f_list):
    result = 0
    t = linspace(0, 1, sample_freq)
    for freq_i in f_list:
        result += sin(2 * pi * freq_i * t)
    return result / len(f_list)


def insert_watermark(dti_param, sample_freq):
    d = sqrt(var(dti[60000:62048])) * 0.25
    s = signal(sample_freq, [20100, 21000])[0:2048]
    s = s[0:2048] * d
    for i in range(0, 2048):
        dti_param[60000 + i] += s[i]
    return s


def create_filter():
    order = 75
    freq = 0.5
    return firwin(order, freq, pass_zero=False)


fr, dti = read_file()
figure("Clean signal")
voice_fourier = fft(dti)
plot(linspace(0, 24000, len(voice_fourier) / 2), abs(voice_fourier[0:len(voice_fourier) / 2]))

watermark = insert_watermark(dti, fr)

figure("Signal with watermark")
watermark_fourier = fft(dti)
plot(linspace(0, 24000, len(watermark_fourier) / 2), abs(watermark_fourier[0:len(watermark_fourier) / 2]))

c = correlate(dti, watermark, 'full')
figure("Correlation")
plot(c)

b = create_filter()
outN = filtfilt(b, 1, dti)
figure("Watermark found")
out_fourier = fft(outN)
plot(linspace(0, 24000, len(out_fourier) / 2), abs(out_fourier[0:len(out_fourier) / 2]))

show()
