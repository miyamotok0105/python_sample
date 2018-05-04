import cis
import numpy as np
import matplotlib.pyplot as plt

#正弦波の生成
t = np.arange(0,1,1/8000)
a = 0.8
f = 440
y = a * np.sin(2 * np.pi * f * t)

#ラが1秒 周波数440Hz
cis.audioplay(y, 8000)

plt.plot(t[:100], y[:100])
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.show()


