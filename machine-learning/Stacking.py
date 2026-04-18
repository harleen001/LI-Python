import numpy as np
from sklearn.base import clone
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_predict, train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC

class SimpleStacking:
    def __init__(self, base_learners, meta_learner):
        self.base_learners = base_learners
        self.meta_learner = meta_learner
        self.fitted_base_learners = []

    def fit(self, X, y):
        meta_features = []
        self.fitted_base_learners = []

        # Train base learners and generate cross-validated predictions to serve as meta-features
        for base_learner in self.base_learners:
            fitted_learner = clone(base_learner).fit(X, y)
            self.fitted_base_learners.append(fitted_learner)
            preds = fitted_learner.predict(X)
            meta_features.append(preds)

        # Stack meta-features horizontally
        meta_features = np.array(meta_features).T

        # Train the meta-learner on the meta-features
        self.meta_learner.fit(meta_features, y)

    def predict(self, X):
        # Generate meta-features for new data
        meta_features = [learner.predict(X) for learner in self.fitted_base_learners]
        meta_features = np.array(meta_features).T
        #meta_features = np.array(meta_features)
        # Final prediction from meta-learner
        return self.meta_learner.predict(meta_features)