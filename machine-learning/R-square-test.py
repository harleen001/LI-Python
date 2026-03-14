import pandas as pd
from CustomLinearRegression import MyLinearRegression
from CustomR import get_accuracy  # Import your new function

df = pd.read_csv("Pepsi.csv")
model = MyLinearRegression()

# Prepare data
x = df['Year'].values 
y = df['Actual_Price'].values

# Train
model.fit(x, y)

# Get Accuracy
accuracy = get_accuracy(x, y, model)

print(f"Model Accuracy (R²): {accuracy:.4f}")
if accuracy > 0.90:
    print("The model is highly accurate!")
else:
    print("The model might need more data or a different approach.")