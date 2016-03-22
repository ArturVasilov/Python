from scipy.signal import firwin2, lfilter, freqz

from pylab import plot, figure

from numpy import pi, linspace, sin

from numpy.fft import fft

ORDER = 125


def signal(f_sample, f_list):
    result = 0
    t = linspace(0, 1, f_sample)
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


sin_list = [15, 40, 60, 90]
fir_filter = multiple_bandpass_fir_filter([(40, 60)], max(sin_list))
w, h = freqz(fir_filter)

figure("Filter")
plot(w / pi, abs(h))

test_signal = signal(200, sin_list)
s = fft(test_signal)
figure("Before filtration")
plot(abs(s)[1: len(s) / 2])

filtered_signal = lfilter(fir_filter, 1, test_signal)
s = fft(filtered_signal)
figure("After filtration")
plot(abs(s)[1: len(s) / 2])
