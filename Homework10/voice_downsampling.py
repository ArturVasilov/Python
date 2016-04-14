from numpy import arange
from pylab import show

from signals.lesson10.utils import write_wav_file, read_wav_file, draw_signal

[fr, dti] = read_wav_file('D:\\voice.wav')

size = len(dti)
M = 2
down_dti = dti[arange(0, size, M)]

draw_signal(dti, fr / 2, 'Original signal')
draw_signal(down_dti, fr / 2, 'Downsampled signal')

write_wav_file('D:\\voice2.wav', fr, down_dti)

show()
