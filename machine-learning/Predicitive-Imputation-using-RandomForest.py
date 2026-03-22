from sklearn.ensemble import RandomForestRegressor
from sklearn.impute import SimpleImputer
import pandas as pd
# Creating dataset with null value
data = pd.DataFrame({
    'Age': [25, 27, None, 35, 40],
    'Income': [50000, None, 45000, 75000, 80000]
})
# Step 1: Filling null values with mean
initial_imputer = SimpleImputer(strategy='mean')
data_imputed = initial_imputer.fit_transform(data)
# Step 2: Set up the model
rf_imputer = RandomForestRegressor()

rf_imputer.fit(data_imputed[~pd.isnull(data['Income'])], data['Income'].dropna())
missing_income = rf_imputer.predict(data_imputed[pd.isnull(data['Income'])])
# Fill the missing values in the original dataset
data.loc[pd.isnull(data['Income']), 'Income'] = missing_income
print(data)