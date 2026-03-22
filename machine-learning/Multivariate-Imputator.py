from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
import pandas as pd
import numpy as np
# Sample dataset creating with null values
data = pd.DataFrame({
    'Age': [25, 27, np.nan, 35, 40],
    'Income': [50000, 52000, 45000, np.nan, 80000],
    'Education': [16, 14, 15, 16, np.nan]
})
imputer = IterativeImputer(max_iter=10, random_state=0)
# Apply imputer to data
imputed_data = imputer.fit_transform(data)
# Convert imputed data to a DataFrame
data_imputed = pd.DataFrame(imputed_data, columns=data.columns)
print(data_imputed)