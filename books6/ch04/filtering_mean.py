
import numpy as np
import scipy.ndimage
from scipy.misc.pilutil import Image


img = Image.open("../dog1.jpeg").convert('L')
# The filter k is a numpy array of size 5 by 5, with all values = 1/25.
kernel = np.ones((5, 5)) / 25
b = scipy.ndimage.filters.convolve(img, kernel)
b = scipy.misc.toimage(b)
b.save("../dog2.jpeg")
