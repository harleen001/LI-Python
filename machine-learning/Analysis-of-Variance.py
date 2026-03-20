from sklearn.feature_selection import SelectKBest, f_classif,chi2
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
import pandas as pd

iris = load_iris()
X = pd.DataFrame(iris.data, columns=iris.feature_names)
y = iris.target
# Apply ANOVA
anova_selector = SelectKBest(f_classif, k=2)
X_kbest_anova = anova_selector.fit_transform(X, y)

# Visualize selected features
selected_features_anova = X.columns[anova_selector.get_support()]
plt.bar(selected_features_anova, anova_selector.scores_[anova_selector.get_support()])
plt.title('ANOVA Feature Importance')
plt.xlabel('Features')
plt.ylabel('F-Values')
plt.show()