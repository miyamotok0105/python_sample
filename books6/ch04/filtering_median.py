
import numpy as np
import scipy.ndimage
from scipy.misc.pilutil import Image

# Median filter is one of the most popular non-linear filters.
# A sliding window is chosen and is placed on the image at the pixel position (i, j).

# Median is a value that divides the list into two equal halves.

img = Image.open("../dog1.jpeg").convert('L')
# performing the median filter
b = scipy.ndimage.filters.median_filter(img, size=5, footprint=None, output=None, mode='reflect', cval=0.0, origin=0)
b = scipy.misc.toimage(b)
b.save("../dog2.jpeg")
