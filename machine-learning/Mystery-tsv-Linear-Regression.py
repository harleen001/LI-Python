import pandas as pd
from sklearn.linear_model import LinearRegression

def mystery_data(file_path):
    df = pd.read_csv(file_path, sep='\t', encoding='unicode_escape')
    
    X = df.iloc[:, :5]
    y = df.iloc[:, -1]
    model = LinearRegression(fit_intercept=False)
    model.fit(X, y)
    
    return model.coef_

file_name = "mystery-data.tsv"
coeffs = mystery_data(file_name)

print(f"Coefficient of X1 is {coeffs[0]}")
print(f"Coefficient of X2 is {coeffs[1]}")
print(f"Coefficient of X3 is {coeffs[2]}")
print(f"Coefficient of X4 is {coeffs[3]}")
print(f"Coefficient of X5 is {coeffs[4]}")

print("\nWhich features you think are needed to explain the response Y?")
needed_features = [f"X{i+1}" for i, c in enumerate(coeffs) if abs(c) > 1e-3]
print(f"Based on the results, the features needed are: {', '.join(needed_features)}")