import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

temperature = np.array([20, 25, 30, 35, 40, 45]).reshape(-1, 1)  
sales = np.array([200, 250, 400, 450, 600, 650])  
df=pd.Series(temperature.flatten(),sales)

model = LinearRegression()
model.fit(temperature, sales)
predicted_sales = model.predict(temperature)

plt.scatter(temperature, sales, color='blue', label="Actual Sales")  # Data points
plt.plot(temperature, predicted_sales, color='red', linestyle='--', label="Regression Line")  # Best fit line
plt.xlabel("Temperature (°C)")
plt.ylabel("Ice Cream Sales (Rs)")
plt.title("Temperature vs Ice Cream Sales Prediction")
plt.legend()
plt.show()


newvalues=np.array([21,32,34,41,42,51]).reshape(-1, 1)
predicted_sales = model.predict(newvalues)

plt.scatter(temperature, sales, color='blue', label="Actual Sales")  
plt.plot(temperature, predicted_sales, color='red', linestyle='--', label="Regression Line") 
plt.xlabel("Temperature (°C)")
plt.ylabel("Ice Cream Sales (Rs)")
plt.title("Temperature vs Ice Cream Sales Prediction")
plt.legend()
plt.show()