#Lasso Regression adds a penalty to the model for large coefficients, 
# effectively shrinking some coefficients to zero, thereby performing feature selection.
from sklearn.linear_model import Lasso
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris

iris = load_iris()
X = pd.DataFrame(iris.data, columns=iris.feature_names)
y = iris.target

# Apply Lasso Regression
lasso = Lasso(alpha=0.1)
lasso.fit(X, y)

# Visualize selected features
plt.bar(X.columns, lasso.coef_)
plt.title('Lasso Regression Feature Importance')
plt.xlabel('Features')
plt.ylabel('Coefficients')
plt.show()