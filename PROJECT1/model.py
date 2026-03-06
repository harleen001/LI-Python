import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

# Load your dataset
df = pd.read_csv("ML.csv")  # Make sure this file is available in the same folder

# Prepare features and target
X = df[["year"]]
y = df["consumption"]

# Train the model
model = LinearRegression()
model.fit(X, y)

# Save the trained model to a .pkl file
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ model.pkl file generated successfully.")
