# Import function to automatically create polynomial features!
from sklearn.preprocessing import PolynomialFeatures
# Import Linear Regression and a regularized regression function
from sklearn.linear_model import LinearRegression, Lasso
from sklearn.linear_model import LassoCV
# Finally, import function to make a machine learning pipeline
from sklearn.pipeline import make_pipeline

from sklearn.linear_model import Ridge
import numpy as np

import matplotlib.pyplot as plt


# Defined data
X_train = [30, 46, 60, 65, 77, 95]
y_train = [31, 30, 80, 49, 70, 118]

X_test = [17, 40, 55, 57, 70, 85]
y_test = [19, 50, 60, 32, 90, 110]
import warnings

# Ignore all warnings
warnings.filterwarnings("ignore")

import pandas as pd
from sklearn.linear_model import Ridge, LinearRegression
from sklearn.preprocessing import PolynomialFeatures, scale

#Confusingly, the lambda term can be configured via the “alpha” argument when defining the class. The default value is 1.0 or a full penalty.

degree_=4
lambda_=0.5

# scale the X data to prevent numerical errors.
X_train = np.array(X_train).reshape(-1, 1)

polyX = PolynomialFeatures(degree=degree_).fit_transform(X_train)

model1 = LinearRegression().fit(polyX, y_train)
model2 = Ridge(alpha=lambda_).fit(polyX, y_train)

# print("OLS Coefs: " + str(model1.coef_[0]))
# print("Ridge Coefs: " + str(model2.coef_[0]))

print(f"Linear Coefs: {sum(model1.coef_)}")
print(f"Ridge Coefs: {sum(model2.coef_)}")


t_ = np.array(np.linspace(0, 120, 120)).reshape(-1, 1)
t = PolynomialFeatures(degree=degree_).fit_transform(t_)



# visualize
plt.plot(X_train, y_train, 'o', t, model2.predict(t), '-')
# plt.scatter(X_train, y_train, color='blue', label='Training set')
# plt.scatter(X_test, y_test, color='red', label='Test set')
plt.legend(loc='best')
plt.ylim((0,120))
plt.xlim((0,120))
plt.show()