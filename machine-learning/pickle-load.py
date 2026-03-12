import numpy as np
import pickle

with open('speed_price_model.pkl', 'rb') as f:
    slope, intercept = pickle.load(f)

x = np.array([15, 20, 30, 40, 50])
predicted_prices = slope * x + intercept

for s, p in zip(x, predicted_prices):
    print(f"Speed: {s} -> Predicted Price: {p:.2f}")