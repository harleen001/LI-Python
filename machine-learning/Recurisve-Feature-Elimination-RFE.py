#RFE recursively removes the least important features and builds the model with 
# the remaining features, iterating until the optimal subset is found.

from sklearn.feature_selection import RFE
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
import pandas as pd


iris = load_iris()
X = pd.DataFrame(iris.data, columns=iris.feature_names)
y = iris.target
# Apply RFE
rfe_selector = RFE(estimator=RandomForestClassifier(), n_features_to_select=2)
X_rfe = rfe_selector.fit_transform(X, y)

# Visualize selected features
selected_features_rfe = X.columns[rfe_selector.get_support()]
plt.bar(selected_features_rfe, rfe_selector.ranking_[rfe_selector.get_support()])
plt.title('RFE Selected Features')
plt.xlabel('Features')
plt.ylabel('Ranking')
plt.show()