import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv("linear_regression_datasets/icecream_sales.csv")

X = df[['Temperature']]  # Independent variable (Temperature)
y = df['Sales']          # Dependent variable (Ice Cream Sales)

model = LinearRegression()
model.fit(X, y)

while True:
    try:
        temperature_input = float(input("Enter temperature (°C) or type 'no' to exit: "))
        predicted_sales = model.predict([[temperature_input]])
        print(f"Predicted Ice C 8 ream Sales: ${predicted_sales[0]:.2f}")
    except ValueError:
        print("Exiting...")
        break