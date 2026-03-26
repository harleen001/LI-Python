import pandas as pd
import math
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder, StandardScaler

# 1. Loading and Encoding
df = pd.read_csv("loan_data.csv")
le = LabelEncoder()
df['person_home_ownership'] = le.fit_transform(df['person_home_ownership'])

# 2. Feature Selection
features = ['person_age', 'person_income', 'person_home_ownership', 'loan_amnt', 'credit_score']
X = df[features]
y = df['loan_status']

# 3. Scaling (Essential for Logistic Regression)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 4. Splitting Data (80:20)
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, train_size=0.8, random_state=42)

# 5. Model Training
model = LogisticRegression()
model.fit(X_train, y_train)

accuracy = model.score(X_test, y_test)
print(f"The Accuracy of the model is = {accuracy:.2%}")

intercept = model.intercept_[0]
coeffs = model.coef_[0]

plt.figure(figsize=(8, 5))
plt.bar(features, coeffs, color=['red' if c > 0 else 'green' for c in coeffs])
plt.axhline(0, color='black', lw=1)
plt.title("Feature Impact on Loan Status (Red = Higher Risk, Green = Lower Risk)")
plt.ylabel("Coefficient Weight")
plt.show()

# --- PREDICTION LOGIC ---
def sigmoid(z):
    return 1 / (1 + math.exp(-z))

def loan_prediction(age, income, home, loan_amt, score):
    input_data = pd.DataFrame([[age, income, home, loan_amt, score]], columns=features)
    scaled_input = scaler.transform(input_data)[0]
    
    # Calculate Z = sum(m*x) + c
    z = sum(coeffs[i] * scaled_input[i] for i in range(len(coeffs))) + intercept
    prob_status_1 = sigmoid(z)

    actual_approval_prob = 1 - prob_status_1 
    return actual_approval_prob

# TESTING
prob = loan_prediction(35, 150000, 2, 5000, 800)
print(f"Approval Probability: {prob:.4f}")
print("Final Result:", "Loan Approved" if prob > 0.5 else "Loan Rejected")