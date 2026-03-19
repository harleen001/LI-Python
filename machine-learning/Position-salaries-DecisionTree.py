import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.tree import DecisionTreeRegressor

#dataset imported and x, y splitted
dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:, 1:-1].values
y = dataset.iloc[:, -1].values


regressor = DecisionTreeRegressor(random_state = 0)   #model created
regressor.fit(X, y)    #trained
regressor.predict([[6.5]])    #tested

X_grid = np.arange(np.min(X), np.max(X), 0.01)   #xgrid and then plotted
X_grid = X_grid.reshape((len(X_grid), 1))
plt.scatter(X, y, color = 'red')
plt.plot(X_grid, regressor.predict(X_grid), color = 'blue')
plt.title('Truth or Bluff (Decision Tree Regression)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()