import numpy as np
from sklearn.cluster import MeanShift
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt

# Generate synthetic data with three blobs
X, _ = make_blobs(n_samples=200, centers=3, cluster_std=0.7)

# Apply Mean Shift clustering
clustering = MeanShift(bandwidth=2).fit(X)
labels = clustering.labels_
cluster_centers = clustering.cluster_centers_

# Plot the results
plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis')
plt.scatter(cluster_centers[:, 0], cluster_centers[:, 1], s=200, c='red', marker='X')
plt.title('Mean Shift Clustering')
plt.show()