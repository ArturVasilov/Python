from numpy import real, var, argmin
from numpy.core.multiarray import zeros
from numpy.fft import fft, ifft
from numpy.linalg import solve
from pylab import show, figure, plot, legend
from scipy.signal import lfilter

from signals.utils.utils import read_wav_file


def lcp(r_param, k_param):
    matrix_a = zeros((k_param, k_param))
    f_vector = zeros(k_param)
    for i in range(0, k_param):
        l = 0
        j = i
        matrix_a[l][j] = r_param[i]
        matrix_a[k_param - l - 1][k_param - j - 1] = r_param[i]
        while j > 0:
            l += 1
            j -= 1
            matrix_a[l][j] = r_param[i]
            matrix_a[k_param - l - 1][k_param - j - 1] = r_param[i]
        f_vector[i] = r_param[i + 1]

    a_vector = solve(matrix_a, f_vector)
    sig_predicted = lfilter(a_vector, 1, dti)
    error = dti - sig_predicted
    dispersion = var(error)

    return a_vector, sig_predicted, dispersion


fr, dti = read_wav_file('D:\\voice.wav')

dti = dti[300000:302048]
for index in range(1024, 2048):
    dti[index] = 0

f = fft(dti)
f **= 2
r = real(ifft(f))
dti = dti[0:1024]

start = 3
end = 101
dispersions = zeros(end - start)

for k in range(start, end):
    a, p, d = lcp(r, k)
    dispersions[k - 3] = d

figure("Dispersions")
plot(dispersions)

best = argmin(dispersions)  # 11 for these conditions
print "Best parameters count = %d" % best
best_coef, predicted, d = lcp(r, best)
sig_lf = lfilter(best_coef, 1, dti)

figure("Signals")
plot(dti, color='blue', label='Original')
plot(predicted, color='red', label='Predicted')
legend()

show()
