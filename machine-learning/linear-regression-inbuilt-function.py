import numpy as np
import matplotlib.pyplot as plt

speed = np.array([10,9,11,12,6,5,7,6,12,14])
price = np.array([95,90,90,105,75,75,80,85,110,115])

slope, intercept = np.polyfit(speed, price, 1)

y_pred = slope * speed + intercept

print(f"Regression Equation: y = {slope:.2f}x + {intercept:.2f}")

plt.scatter(speed, price, color='blue', label='Actual Data Points')
plt.plot(speed, y_pred, color='red', linewidth=2, label='Linear Regression Line')
plt.xlabel('Speed (Independent Variable)')
plt.ylabel('Price (Dependent Variable)')
plt.title('Linear Regression using NumPy')
plt.legend()
plt.show()