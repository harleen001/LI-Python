from sklearn.base import clone
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
import numpy as np
from scipy.stats import mode
class SimpleBag:
    def __init__(self, base_estimator=None, n_estimators=10, subset_size=0.8):
        self.base_estimator = base_estimator if base_estimator else DecisionTreeClassifier(max_depth=1, max_features=1)
        self.n_estimators = n_estimators
        self.subset_size = subset_size
        self.base_learners = []
        self.is_fitted = False

    def fit(self, X, y):
        n_samples = X.shape[0]
        subset_size = int(n_samples * self.subset_size)
        self.base_learners = []

        for _ in range(self.n_estimators):
            indices = np.random.choice(range(n_samples), size=subset_size, replace=True)
            X_subset, y_subset = X[indices], y[indices]
            cloned_estimator = clone(self.base_estimator)
            cloned_estimator.fit(X_subset, y_subset)
            self.base_learners.append(cloned_estimator)

        self.is_fitted = True

    def predict(self, X):
        if not self.is_fitted:
            raise Exception("This SimpleBag instance is not fitted yet.")

        predictions = np.array([learner.predict(X) for learner in self.base_learners]).T
        final_predictions, _ = mode(predictions, axis=1)
        return final_predictions.ravel()

# Load data
X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train and evaluate a single Decision Tree
single_tree = DecisionTreeClassifier(max_depth=1, max_features=1)
single_tree.fit(X_train, y_train)
single_tree_predictions = single_tree.predict(X_test)
single_tree_accuracy = accuracy_score(y_test, single_tree_predictions)

# Initialize, fit, and evaluate the SimpleBag model
simple_bag = SimpleBag(n_estimators=100, subset_size=0.5)
simple_bag.fit(X_train, y_train)
simple_bag_predictions = simple_bag.predict(X_test)
simple_bag_accuracy = accuracy_score(y_test, simple_bag_predictions)

print(f'Accuracy of the single Decision Tree model: {single_tree_accuracy:.2f}')
print(f'Accuracy of the SimpleBag ensemble model: {simple_bag_accuracy:.2f}')
