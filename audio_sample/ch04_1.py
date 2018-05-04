import cis
import numpy as np
import scipy.fftpack as sfft
import scipy.signal as ss
import matplotlib.pyplot as plt

#線形フィルター
fs = 8000
t = np.arange(0,1,1/fs)
s = np.sin(2 * np.pi * 800 * t) + np.sin(2 * np.pi * 500 * t)
cis.audioplay(s,fs)

rg = np.arange(0,100)
plt.subplot(3,1,1);plt.plot(s[rg])
sd = np.roll(s, 5)
plt.subplot(3,1,2);plt.plot(sd[rg])
cis.audioplay(sd,fs)
ssd = s + sd
plt.subplot(3,1,3);plt.plot(ssd[rg])
cis.audioplay(ssd,fs)
plt.show()

#打ち消しあって成分が除去された。
#一般的にはある成分を除去することが多いためフィルターと呼ばれる