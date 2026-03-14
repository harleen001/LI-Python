import pandas as pd
from CustomLinearRegression import MyLinearRegression
from CustomR import get_accuracy
import numpy as np

df = pd.read_csv("Pepsi.csv")
model = MyLinearRegression()

x = df['Year'].values 
y = df['Actual_Price'].values
model.fit(x, y)
y_pred = model.predict(x)

df['Predicted_Price'] = y_pred

print(df.head(10))

new_x=np.array([2026,2027,2028,2029,2030])
new_prices=model.predict(new_x)

future_df = pd.DataFrame({'Year': new_x,'Actual_Price': np.nan,'Predicted_Price': new_prices})

df = pd.concat([df, future_df], ignore_index=True)
print(df.head(15))


accuracy = get_accuracy(x, y, model)

print(f"Model Accuracy (R²): {accuracy:.4f}")
if accuracy > 0.90:
    print("The model is highly accurate!")
else:
    print("The model might need more data or a different approach.")