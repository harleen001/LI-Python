#Gradient decent is an algorithm to minimum your function by optimizing its parameter
from sklearn.datasets import make_regression
import numpy as np
X,y = make_regression(n_samples=4, n_features=1, n_informative=1, n_targets=1,noise=80,random_state=13)
import matplotlib.pyplot as plt
plt.scatter(X,y)
plt.show()