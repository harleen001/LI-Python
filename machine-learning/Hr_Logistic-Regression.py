import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

df = pd.read_csv("HR_Logistic_Regression.csv")

subdf = df[['satisfaction_level', 'average_montly_hours', 'promotion_last_5years', 'salary']]
salary_dummies = pd.get_dummies(subdf.salary, prefix="salary")
X = pd.concat([subdf, salary_dummies], axis='columns').drop('salary', axis='columns')
y = df.left

X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.3, random_state=42)

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

print(f"Accuracy: {model.score(X_test, y_test)}")

new_data = pd.DataFrame([
    [0.1, 280, 0, 0, 1, 0], # Employee 1
    [0.9, 150, 1, 1, 0, 0]  # Employee 2
], columns=X.columns)

# Now predict using the DataFrame
predictions = model.predict(new_data)
probabilities = model.predict_proba(new_data)

for i, pred in enumerate(predictions):
    status = "Leaving" if pred == 1 else "Staying"
    chance = probabilities[i][1] * 100
    print(f"Employee {i+1}: Predicted to {status} ({chance:.2f}% probability)")