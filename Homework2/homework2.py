import pylab as plb
from scipy.io.wavfile import read

from utils import zero_crossing_counts_list

voice_file = open('voice.wav', 'rb')
[fr, dti] = read(voice_file)
voice_file.close()

zero_crossing = zero_crossing_counts_list(dti, 0.5, 256)

plb.figure()

plb.plot(zero_crossing)
