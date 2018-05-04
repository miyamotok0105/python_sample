import cis
import numpy as np
import matplotlib.pyplot as plt

#時間波形の連結
fs = 8000
a = 0.4
t = np.arange(0,1,1/fs)
y523 = a * np.sin(2 * np.pi * 523 * t)
y660 = a * np.sin(2 * np.pi * 660 * t)
cis.audioplay(np.vstack((y523, y660)), fs)

# r = np.arange(200)
# plt.plot(t[r], yy[r])
# plt.show()

