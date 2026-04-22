import numpy as np
from collections import Counter

class KNearestNeighbors:
    def __init__(self, k=3):
        self.k = k

    def fit(self, X, y):
        self.X_train = X
        self.y_train = y

    def predict(self, X):
        predictions = [self._predict(x) for x in X]
        return np.array(predictions)

    def _predict(self, x):
        # Calculate distances between x and all training examples
        distances = [self._euclidean_distance(x, x_train) for x_train in self.X_train]

        # Get the k nearest neighbors
        k_indices = np.argsort(distances)[:self.k]
        k_nearest_labels = [self.y_train[i] for i in k_indices]

        # Return the most common class label among the k nearest neighbors
        most_common = Counter(k_nearest_labels).most_common(1)
        return most_common[0][0]

    def _euclidean_distance(self, x1, x2):
        return np.sqrt(np.sum((x1 - x2)**2))

# Example Usage:
if __name__ == "__main__":
    # Sample data
    X_train = np.array([[1, 1], [1, 2], [2, 2], [5, 5], [5, 6], [6, 6]])
    y_train = np.array([0, 0, 0, 1, 1, 1]) # 0 for class A, 1 for class B

    # New data point to classify
    X_test = np.array([[1.5, 1.5], [5.5, 5.5], [3, 3]])

    # Initialize and train the KNN classifier
    knn = KNearestNeighbors(k=3)
    knn.fit(X_train, y_train)

    # Make predictions
    predictions = knn.predict(X_test)
    print(f"Predictions for new data points: {predictions}")