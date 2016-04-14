from numpy import arange, zeros
from pylab import show

from signals.lesson10.utils import write_wav_file, read_wav_file, draw_signal

[fr, dti] = read_wav_file('D:\\voice.wav')

size = len(dti)
M = 2
up_dti = zeros(size * M)
up_dti[arange(0, size * M, M)] = dti

draw_signal(dti, fr / 2, 'Original signal')
draw_signal(up_dti, fr / 2, 'Upsampled signal')

write_wav_file('D:\\voice2.wav', fr, up_dti)

show()
