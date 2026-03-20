import pandas as pd
from sklearn.datasets import load_iris
from sklearn.feature_selection import SelectKBest, chi2
import matplotlib.pyplot as plt

# Load Iris dataset
iris = load_iris()
X = pd.DataFrame(iris.data, columns=iris.feature_names)
y = iris.target
# Apply Chi-Square test
chi2_selector = SelectKBest(chi2, k=2)
X_kbest = chi2_selector.fit_transform(X, y)

# Visualize selected features
selected_features = X.columns[chi2_selector.get_support()]
plt.bar(selected_features, chi2_selector.scores_[chi2_selector.get_support()])
plt.title('Chi-Square Test Feature Importance')
plt.show()