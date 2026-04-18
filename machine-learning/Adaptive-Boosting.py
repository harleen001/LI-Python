from sklearn.base import BaseEstimator, ClassifierMixin, clone
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
import numpy as np

class SimpleMultiClassBoosting(BaseEstimator, ClassifierMixin):
    def __init__(self, base_estimator=None, n_estimators=50):
        self.base_estimator = base_estimator if base_estimator is not None else DecisionTreeClassifier(max_depth=1)
        self.n_estimators = n_estimators
        self.learners = []
        self.learner_weights = []
        self.label_encoder = LabelEncoder()

    def fit(self, X, y):
        # Convert labels to [0, n_classes-1]
        y_encoded = self.label_encoder.fit_transform(y)
        n_classes = len(self.label_encoder.classes_)

        # Initialize weights uniformly
        sample_weights = np.full(X.shape[0], 1 / X.shape[0])

        for _ in range(self.n_estimators):
            learner = clone(self.base_estimator)
            learner.fit(X, y_encoded, sample_weight=sample_weights)
            learner_pred = learner.predict(X)

            # Compute weighted error rate (misclassification rate)
            incorrect = (learner_pred != y_encoded)
            learner_error = np.mean(np.average(incorrect, weights=sample_weights))

            # Compute learner weight using SAMME algorithm
            learner_weight = np.log((1 - learner_error) / (learner_error + 1e-10)) + np.log(n_classes - 1)
            if learner_error >= 1 - (1 / n_classes):
                break  # Stop if the learner is no better than random guessing

            # Increase the weights of misclassified samples
            sample_weights *= np.exp(learner_weight * incorrect * (sample_weights > 0))
            sample_weights /= np.sum(sample_weights)  # Normalize weights

            # Save the current learner
            self.learners.append(learner)
            self.learner_weights.append(learner_weight)

    def predict(self, X):
        # Collect predictions from each learner
        learner_preds = np.array([learner.predict(X) for learner in self.learners])

        # Weighted vote for each sample's prediction across all learners
        weighted_preds = np.zeros((X.shape[0], len(self.label_encoder.classes_)))
        for i in range(len(self.learners)):
            weighted_preds[np.arange(X.shape[0]), learner_preds[i]] += self.learner_weights[i]

        # Final prediction is the one with the highest weighted vote
        y_pred = np.argmax(weighted_preds, axis=1)
        # Convert back to original class labels
        return self.label_encoder.inverse_transform(y_pred)
