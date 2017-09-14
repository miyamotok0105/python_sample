# -*- coding: utf-8 -*-
from sklearn.cluster import KMeans

import numpy as np
X = np.array([[1, 2], [1, 4], [1, 0],[4, 2], [4, 4], [4, 0]])
kmeans = KMeans(n_clusters=2, random_state=0).fit(X)

print("各点のラベル:")
print(kmeans.labels_)
print("近いクラスターの推定:")
print(kmeans.predict([[0, 0], [4, 4]]))
print("クラスターの中央:")
print(kmeans.cluster_centers_)