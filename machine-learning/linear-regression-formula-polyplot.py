import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

speed = np.array([10,9,11,12,6,5,7,6,12,14]).reshape(-1,1)
price = np.array([95,90,90,105,75,75,80,85,110,115])

model=LinearRegression()
model.fit(speed,price)

y_pred=model.predict(speed)


#y_pred = slope * speed + intercept

plt.scatter(speed, price, color='blue', label='Actual Data Points')
plt.plot(speed, y_pred, color='red', linewidth=2, label='Linear Regression Line')
plt.xlabel('Speed (Independent Variable)')
plt.ylabel('Price (Dependent Variable)')
plt.title('Linear Regression using NumPy')
plt.legend()
plt.show()