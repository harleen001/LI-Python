import pandas as pd
import math
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder, StandardScaler

df = pd.read_csv("loan_data.csv")  #dataset
le = LabelEncoder()   #label encoded for columns
df['person_home_ownership'] = le.fit_transform(df['person_home_ownership'])

#features selected
features = ['person_age', 'person_income', 'person_home_ownership', 'loan_amnt', 'credit_score']
X = df[features]   #x and y selected
y = df['loan_status']

scaler = StandardScaler()  #data standardised
X_scaled = scaler.fit_transform(X)

# data splitted into 80:20 for test and train
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, train_size=0.8, random_state=42)

#logistic model created, trained and then predicted for values
model = LogisticRegression()
model.fit(X_train, y_train)

intercept = model.intercept_[0]
coeffs = model.coef_[0]

def sigmoid(z):  #sigmoid function created
    return 1 / (1 + math.exp(-z))

def loan_prediction(age, income, home, loan_amt, score):
    input_data = pd.DataFrame([[age, income, home, loan_amt, score]], columns=features)
    scaled_input = scaler.transform(input_data)[0]
    
    z = sum(coeffs[i] * scaled_input[i] for i in range(len(coeffs))) + intercept
    prob_status_1 = sigmoid(z)
    
    actual_approval_prob = 1 - prob_status_1 
    return actual_approval_prob

prob = loan_prediction(35, 150000, 2, 5000, 800)

print(f"Approval Probability: {prob:.4f}")
print("Final Result:", "Loan Approved" if prob > 0.5 else "Loan Rejected")