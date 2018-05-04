import cis
import numpy as np
import matplotlib.pyplot as plt

#時間波形の重ね合わせ
fs = 8000
t = np.arange(0,1,1/fs)
a = 0.3
y523 = a * np.sin(2 * np.pi * 523 * t)
y660 = a * np.sin(2 * np.pi * 660 * t)
y784 = a * np.sin(2 * np.pi * 784 * t)
yy = y523 + y660 + y784

cis.audioplay(yy, fs)

r = np.arange(200)
plt.plot(t[r], yy[r])
plt.show()

#時間波形の重ね合わせ　うなり

a = 0.4
t = np.arange(0,1,1/fs)
y438 = a * np.sin(2 * np.pi * 438 * t)
y442 = a * np.sin(2 * np.pi * 442 * t)
cis.audioplay(y438+y442, fs)
