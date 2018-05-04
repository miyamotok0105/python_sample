import cis
import numpy as np
import scipy.fftpack as sfft
import scipy.signal as ss
import matplotlib.pyplot as plt

#フーリエ変換
fs = 100
t = np.arange(0,7,1/fs)
y = np.sin(2 * np.pi * 15 * t) + np.cos(2 * np.pi * 40 * t)
cs = sfft.fft(y[:600])

plt.plot(np.abs(cs))
plt.show()

