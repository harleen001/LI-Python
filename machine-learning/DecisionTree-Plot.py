import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
from sklearn.tree import plot_tree 

X = np.array([[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]])   # x and y coordinates
y = np.array([4.5, 5.2, 6.1, 7.3, 8.5, 9.1, 10.2, 11.5, 12.8, 13.9])

#train test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
regressor = DecisionTreeRegressor(random_state=0, max_depth=3) #regressor with depth specified
regressor.fit(X_train, y_train) #train model
y_pred = regressor.predict(X_test)   #test for y_pred on x_test

mse = mean_squared_error(y_test, y_pred)   # mean squared error test
print(f"Mean Squared Error: {mse:.2f}")  #print mean squared error

plt.figure(figsize=(12, 8))
plot_tree(regressor, filled=True, rounded=True, feature_names=["Feature_Name"], fontsize=10)
plt.title("Decision Tree Regressor")
plt.show()