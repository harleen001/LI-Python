# my_models.py
import numpy as np

class MyLinearRegression:
    def __init__(self):
        self.slope = None
        self.intercept = None

    def fit(self, x, y):
        x = np.array(x).flatten()
        y = np.array(y).flatten()
        x_mean = np.mean(x)
        y_mean = np.mean(y)
       
        # Calculate slope (m) using the OLS formula: 
        # m = sum((x - x_mean) * (y - y_mean)) / sum((x - x_mean)^2)
        numerator = np.sum((x - x_mean) * (y - y_mean))
        denominator = np.sum((x - x_mean)**2)
        
        self.slope = numerator / denominator
        
        # Calculate intercept (b): b = y_mean - m * x_mean
        self.intercept = y_mean - (self.slope * x_mean)

    def predict(self, x):
        return self.slope * np.array(x) + self.intercept