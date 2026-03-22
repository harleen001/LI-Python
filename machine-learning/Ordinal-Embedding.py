import pandas as pd
from sklearn.preprocessing import OrdinalEncoder
data = pd.DataFrame({
    'Quality': ['Low', 'Medium', 'High', 'Medium', 'Low']
})
encoder = OrdinalEncoder(categories=[['Low', 'Medium', 'High']])
data['Quality_encoded'] = encoder.fit_transform(data[['Quality']])
print(data)