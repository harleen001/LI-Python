# Lets apply OLS
from sklearn.linear_model import LinearRegression
from sklearn.datasets import make_regression
import matplotlib.pyplot as plt

reg = LinearRegression()
X,y = make_regression(n_samples=4, n_features=1, n_informative=1, n_targets=1,noise=80,random_state=13)

reg.fit(X,y)
# plt.scatter(X,y)
# plt.plot(X,reg.predict(X),color='red')


# Lets apply Gradient Descent assuming slope is constant m = 78.35
# and let's assume the starting value for intercept b = 0
y_pred = ((78.35 * X) + 100).reshape(4)

# plt.scatter(X,y)
# plt.plot(X,reg.predict(X),color='red',label='OLS')
# plt.plot(X,y_pred,color='#00a65a',label='b = 0')
# plt.legend()
# plt.show()

import numpy as np
# next iteration
m = 78.35
b = 100

loss_slope = -2 * np.sum(y - m*X.ravel() - b)
loss_slope
# Lets take learning rate = 0.1
lr = 0.1

step_size = loss_slope*lr
step_size
# Calculating the new intercept
b = b - step_size
b

y_pred1 = ((78.35 * X) + b).reshape(4)

plt.scatter(X,y)
plt.plot(X,reg.predict(X),color='red',label='OLS')
plt.plot(X,y_pred1,color='#00a65a',label='b = {}'.format(b))
plt.plot(X,y_pred,color='#A3E4D7',label='b = 0')
plt.legend()
plt.show()


#similar way do multiple iterations OLS