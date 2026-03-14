import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv('ipl_winner.csv')
df['Win_Percentage'] = df['Win_Percentage'].str.replace('%', '').astype(float)

le = LabelEncoder()
all_teams = pd.concat([df['Winner'], df['Runner-up']]).unique()
le.fit(all_teams)

df['Winner_ID'] = le.transform(df['Winner'])
df['Runner_up_ID'] = le.transform(df['Runner-up'])

X = df[['Year', 'Win_Percentage']].values
y = df[['Winner_ID', 'Runner_up_ID']].values

model = LinearRegression()
model.fit(X, y)
test_input = np.array([[2026, 65.0]])
predictions = model.predict(test_input)

def get_team_name(val):
    idx = int(np.round(val))
    idx = max(0, min(idx, len(le.classes_) - 1))
    return le.inverse_transform([idx])[0]

final_winner = get_team_name(predictions[0][0])
final_runner = get_team_name(predictions[0][1])

print(f"--- IPL 2026 Prediction ---")
print(f"Winner: {final_winner}")
print(f"Runner-up: {final_runner}")