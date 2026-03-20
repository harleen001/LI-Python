from sklearn.decomposition import PCA
from sklearn.datasets import load_iris

        # Load sample data
iris = load_iris()
X = iris.data

        # Apply PCA with 2 components
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)
print("Original data shape:", X.shape)
print("Reduced data shape (PCA):", X_pca.shape)