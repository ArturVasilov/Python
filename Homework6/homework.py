from scipy.signal import firwin2, lfilter, freqz

from pylab import plot, figure, show, legend

from numpy import pi, linspace, sin

from numpy.fft import fft

ORDER = 75


def signal(sample_freq, f_list):
    result = 0
    t = linspace(0, 1, sample_freq)
    for freq in f_list:
        result += sin(2 * pi * freq * t)
    return result


def multiple_bandpass_fir_filter(intervals, f_max, order=ORDER):
    freq = [0.0]
    gain = [0]
    current = 0
    for (f_left, f_right) in intervals:
        left = f_left * 1.0 / f_max
        right = f_right * 1.0 / f_max
        if left < (current + 0.01) or left >= right or left > 0.99 or right > 0.99:
            raise Exception("Bad intervals arguments")

        freq.append(left - 0.01)
        freq.append(left)
        freq.append(right)
        freq.append(right + 0.01)

        gain.append(0)
        gain.append(1)
        gain.append(1)
        gain.append(0)

        current = right + 0.01

    freq.append(1)
    gain.append(0)

    return firwin2(order, freq, gain)

f_sample = 200
sin_list = [15, 40, 60, 90]
fir_filter = multiple_bandpass_fir_filter([(40, 60)], f_sample / 2)
w, h = freqz(fir_filter)

figure("Filter")
plot(w / pi, abs(h))

test_signal = signal(f_sample, sin_list)
signal_fourier = fft(test_signal)
filtered_signal = lfilter(fir_filter, 1, test_signal)
filtered_signal_fourier = fft(filtered_signal)

figure("Signal")
plot(abs(signal_fourier[0:len(signal_fourier) / 2]), color='blue', label='After filtration')
plot(abs(filtered_signal_fourier[0:len(filtered_signal_fourier) / 2]), color='red', label='Before filtration')
legend()
show()
