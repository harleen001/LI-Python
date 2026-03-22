import pandas as pd
data = pd.DataFrame({
    'Date': pd.date_range(start='2023-01-01', periods=5, freq='D'),
    'value': [10, 12, 15, 18, 20]
})
data['lag_1'] = data['value'].shift(1)
data['lag_2'] = data['value'].shift(2)
print(data)
data['rolling_var_3'] = data['value'].rolling(window=3).var()
print(data)