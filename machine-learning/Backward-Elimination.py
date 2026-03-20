#Backward elimination begins with all features and removes the least 
# significant ones based on their p-values, refining the model iteratively.
from sklearn.feature_selection import RFECV
from sklearn.datasets import load_iris
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier

iris = load_iris()
X = pd.DataFrame(iris.data, columns=iris.feature_names)
y = iris.target

# Apply Backward Elimination using RFECV
rfecv_selector = RFECV(estimator=RandomForestClassifier(), step=1, cv=5, scoring='accuracy')
X_rfecv = rfecv_selector.fit_transform(X, y)

# Visualize selected features
selected_features_rfecv = X.columns[rfecv_selector.get_support()]
plt.bar(selected_features_rfecv, rfecv_selector.cv_results_['mean_test_score'][rfecv_selector.get_support()])
plt.title('Backward Elimination Features')
plt.xlabel('Features')
plt.ylabel('Cross-Validation Scores')
plt.show()