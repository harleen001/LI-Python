import numpy as np
import matplotlib.pyplot as plt
import pickle

speed = np.array([10, 9, 11, 12, 6, 5, 7, 6, 12, 14])
price = np.array([95, 90, 90, 105, 75, 75, 80, 85, 110, 115])

slope, intercept = np.polyfit(speed, price, 1)

model_data = [slope, intercept]
with open('speed_price_model.pkl', 'wb') as f:
    pickle.dump(model_data, f)

with open('speed_price_model.pkl', 'rb') as f:
    loaded_slope, loaded_intercept = pickle.load(f)

y_pred = loaded_slope * speed + loaded_intercept

print(f"Regression Equation: y = {loaded_slope:.2f}x + {loaded_intercept:.2f}")

plt.scatter(speed, price, color='blue', label='Actual Data Points')
plt.plot(speed, y_pred, color='red', linewidth=2, label='Linear Regression Line')
plt.xlabel('Speed')
plt.ylabel('Price')
plt.title('Linear Regression with Pickle')
plt.legend()
plt.show()