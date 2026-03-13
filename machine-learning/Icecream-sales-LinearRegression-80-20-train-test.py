import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error

df = pd.read_csv("linear_regression_datasets/icecream_sales.csv")  

X = df[['Temperature']]  
y = df['Sales']          


trainX, testX, trainY, testY = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(trainX, trainY)

predictions = model.predict(testX)

mae = mean_absolute_error(testY, predictions)
mse = mean_squared_error(testY, predictions)
rmse = np.sqrt(mse)

print(f"Mean Absolute Error: {mae:.2f}")
print(f"Root Mean Squared Error: {rmse:.2f}")

while True:
    try:
        temperature_input = float(input("Enter temperature (°C) or type 'no' to exit: "))
        predicted_sales = model.predict([[temperature_input]])
        print(f"Predicted Ice Cream Sales: ${predicted_sales[0]:.2f}")
    except ValueError:
        print("Exiting...")
        break