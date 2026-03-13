import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

x = np.array([10,9,11,12,6,5,7,6,12,14]).reshape(-1,1)
y = np.array([95,90,90,105,75,75,80,85,110,115])

def fit_line(x,y):
    model=LinearRegression()
    model.fit(x,y)
    y_pred=model.predict(x)

#y_pred = slope * speed + intercept

    plt.scatter(x, y, color='blue', label='Actual Data Points')
    plt.plot(x, y_pred, color='red', linewidth=2, label='Linear Regression Line')
    plt.xlabel('Speed (Independent Variable)')
    plt.ylabel('Price (Dependent Variable)')
    plt.title('Linear Regression using NumPy')
    plt.legend()
    plt.show()


fit_line(x,y)