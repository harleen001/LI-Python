#Forward selection starts with no features and adds them one by one, 
# based on their contribution to improving the model’s performance.

from mlxtend.feature_selection import SequentialFeatureSelector as SFS 
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_iris
import pandas as pd
import matplotlib.pyplot as plt

iris = load_iris()
X = pd.DataFrame(iris.data, columns=iris.feature_names)
y = iris.target
# Apply Forward Selection
sfs = SFS(KNeighborsClassifier(), k_features=2, forward=True, scoring='accuracy', cv=5)
sfs.fit(X, y)

# Visualize selected features
selected_features_fs = X.columns[list(sfs.k_feature_idx_)]
plt.bar(selected_features_fs, range(len(selected_features_fs)))
plt.title('Forward Selection Features')
plt.xlabel('Features')
plt.ylabel('Selected Order')
plt.show()