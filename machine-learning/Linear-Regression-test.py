import numpy as np
import matplotlib.pyplot as plt
import sklearn 
from sklearn.linear_model import LinearRegression

np.random.seed(0)
n=20  
x=np.linspace(0, 10, n)
y=x*2 + 1 + 1*np.random.randn(n)
print(x)
print(y)

model=LinearRegression(fit_intercept=True)
model.fit(x[:,np.newaxis], y)
xfit=np.linspace(0,10,100)
yfit=model.predict(xfit[:, np.newaxis])
plt.plot(xfit,yfit, color="black")
plt.plot(x,y, 'o')
plt.plot(np.vstack([x,x]), np.vstack([y, model.predict(x[:, np.newaxis])]), color="red")
plt.show()