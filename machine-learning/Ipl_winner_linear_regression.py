import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv('ipl_winner.csv')

le = LabelEncoder()
df['Winner_ID'] = le.fit_transform(df['Winner'])

X = df[['Year']].values
y = df['Winner_ID'].values

model = LinearRegression()
model.fit(X, y)

year_2026 = np.array([[2026]])
predicted_id_float = model.predict(year_2026)[0]
predicted_id = int(np.round(predicted_id_float))
predicted_id = max(0, min(predicted_id, len(le.classes_) - 1))

predicted_winner = le.inverse_transform([predicted_id])[0]

print(f"2026 Prediction: {predicted_winner}")