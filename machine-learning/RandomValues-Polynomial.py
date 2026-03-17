import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

#random x and y
np.random.seed(0)
X = np.random.rand(100, 1)
y = 2 * X + 1 + np.random.randn(100, 1)

#taking degree
degree = 2      
poly_features = PolynomialFeatures(degree=degree)
X_poly = poly_features.fit_transform(X)


#linear regression model fit and predict
model = LinearRegression()
model.fit(X_poly, y)

X_new = np.linspace(0, 1, 100).reshape(-1, 1)
X_new_poly = poly_features.transform(X_new)
y_new = model.predict(X_new_poly)

plt.scatter(X, y, label='Data', color='blue')
plt.plot(X_new, y_new, label='Polynomial Regression', color='red', linewidth=2)
plt.xlabel('X')
plt.ylabel('y')
plt.legend()
plt.title(f'Polynomial Regression (Degree {degree})')
plt.show()