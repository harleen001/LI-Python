from sklearn.cluster import MeanShift, estimate_bandwidth
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
#Sample data points
centers = [[1, .75], [-.75, -1], [1, -1]]
X, _ = make_blobs(n_samples=10000, centers= centers, cluster_std=0.6)
# Bandwidth estimation using in-built function
est_bandwidth = estimate_bandwidth(X, quantile=.1,
n_samples=500)
mean_shift = MeanShift(bandwidth= est_bandwidth, bin_seeding=True)
mean_shift.fit(X)
ms_labels = mean_shift.labels_
c_centers = mean_shift.cluster_centers_
n_clusters_ = len(set(ms_labels))
# Plot result
plt.figure(1)
plt.clf()
colors = "bgrcmykbgrcmykbgrcmykbgrcmyk"
for i, each in zip(range(n_clusters_), colors):
    my_members = ms_labels == i
    cluster_center = c_centers[i]
    plt.plot(X[my_members, 0], X[my_members, 1], each + '.')
    plt.plot(cluster_center[0], cluster_center[1],
             'o', markerfacecolor=each,
             markeredgecolor='k', markersize=14)
plt.title('Estimated cluster numbers: %d'% n_clusters_)
plt.show()