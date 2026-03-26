import pandas as pd
import math
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv("loan_data.csv")  #csv loaded
le = LabelEncoder()   #labels encoded
categorical_cols = ['person_gender', 'person_education', 'person_home_ownership', 'previous_loan_defaults_on_file']

for col in categorical_cols:   #specific categorical variables
    df[col] = le.fit_transform(df[col])

features = ['person_age', 'person_income', 'credit_score']  #multiple features plotted
X = df[features]
y = df['loan_status']

#splittint the data into 80 20 for test and train purpose
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.8, random_state=42)

#logistic model created, model trained on x and y train data and the y= mx+c predicted
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)


intercept = model.intercept_[0]
coeffs = model.coef_[0]

def sigmoid(z):  #sigmoid function created
    return 1 / (1 + math.exp(-z))

def loan_prediction(age, income, score): # age income and score
    z = (coeffs[0] * age) + (coeffs[1] * income) + (coeffs[2] * score) + intercept
    probability = sigmoid(z)
    return probability

test_prob = loan_prediction(22, 71000, 561)
print(f"\nProbability of Loan Status 1: {test_prob:.4f}")
print("Result:", "Loan Approved" if test_prob > 0.5 else "Loan Rejected")