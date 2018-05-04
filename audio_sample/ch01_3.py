import cis
import numpy as np
import matplotlib.pyplot as plt

#時間波形の重ね合わせ　うなり
fs = 8000
a = 0.4
t = np.arange(0,1,1/fs)
y438 = a * np.sin(2 * np.pi * 438 * t)
y442 = a * np.sin(2 * np.pi * 442 * t)
cis.audioplay(y438+y442, fs)


# r = np.arange(200)
# plt.plot(t[r], yy[r])
# plt.show()

