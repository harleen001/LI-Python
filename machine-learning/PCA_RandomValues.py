import numpy as np
import matplotlib.pyplot as plt
import math
from sklearn.decomposition import PCA

# Setup data
rng = np.random.RandomState(0)
X = rng.randn(2, 400)
scale = np.array([[1, 0], [0, 0.4]]) 
rotate = np.array([[1, -1], [1, 1]]) / math.sqrt(2)
transform = np.dot(rotate, scale)
X = np.dot(transform, X).T

# PCA Fit
pca = PCA(2)
pca.fit(X)

def draw_vector(v0, v1, ax=None):
    ax = ax or plt.gca()
    arrowprops = dict(arrowstyle='->', linewidth=2, shrinkA=0, shrinkB=0, color='black')
    ax.annotate('', v1, v0, arrowprops=arrowprops)

# Plotting Original vs Transformed
fig, axes = plt.subplots(1, 2, figsize=(12, 4))

# Left plot: Original data with Principal Component vectors
axes[0].scatter(X[:, 0], X[:, 1], alpha=0.3)
for length, vector in zip(pca.explained_variance_, pca.components_):
    v = vector * 3 * np.sqrt(length) # Scaling for visibility
    draw_vector(pca.mean_, pca.mean_ + v, ax=axes[0])
axes[0].set_title("Original Data & PCA Components")
axes[0].axis('equal')

# Right plot: Data projected onto the PCs (Decorrelated)
Z = pca.transform(X)
axes[1].scatter(Z[:, 0], Z[:, 1], alpha=0.3)
axes[1].set_title("Transformed (Projected) Data")
axes[1].axis('equal')
plt.show()



from sklearn.datasets import load_diabetes

# Fix: return_X_y=True is the correct parameter
X_diab, y_diab = load_diabetes(return_X_y=True)

# Random high-dimensional projection
rng = np.random.RandomState(0)
X_3d = rng.randn(3, 400)
projection_matrix = rng.rand(10, 3) 
X_10d = np.dot(projection_matrix, X_3d).T # Shape (400, 10)

pca_high = PCA().fit(X_10d)
v = pca_high.explained_variance_ratio_ # Using ratio is often clearer
cumulative_variance = np.cumsum(v)

plt.figure(figsize=(8, 4))
plt.plot(np.arange(1, len(v) + 1), cumulative_variance, marker='o')
plt.xlabel('Number of Components')
plt.ylabel('Cumulative Explained Variance')
plt.title('Scree Plot: Identifying the Intrinsic Dimensionality')
plt.grid(True)
plt.show()