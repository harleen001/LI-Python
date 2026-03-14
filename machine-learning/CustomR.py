# metrics_utils.py
import numpy as np

def get_accuracy(x, y, model):
    """
    Calculates the R-squared score.
    x: independent variables
    y: actual valuesn
    model: the trained model instance with a .predict() method
    """
    y = np.array(y)
    y_pred = model.predict(x)
    y_mean = np.mean(y)
    
    # SSR: Sum of Squared Residuals (Error from your line)
    ssr = np.sum((y - y_pred)**2)
    
    # SST: Total Sum of Squares (Total variance in the data)
    sst = np.sum((y - y_mean)**2)
    
    r2 = 1 - (ssr / sst)
    return r2