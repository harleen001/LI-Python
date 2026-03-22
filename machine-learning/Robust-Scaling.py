from sklearn.preprocessing import RobustScaler
import pandas as pd
data = pd.DataFrame({'Feature': [10, 20, 30, 1000, 50]})
scaler = RobustScaler()
data['Scaled_Feature'] = scaler.fit_transform(data[['Feature']])
print(data)