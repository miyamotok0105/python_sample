import numpy as np

src = np.arange(1, 1000)
dest = src[(src % 3 == 0) | (src % 5 == 0)]
sum = np.sum(dest)
print("sum is {sum} ".format(sum=sum))

