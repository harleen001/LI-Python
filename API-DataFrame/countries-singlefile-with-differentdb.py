import requests
import pandas as pd

url = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url)
data = response.json()

df = pd.json_normalize(data)

df = df[['id', 'name', 'username', 'email', 'address.city']]
df.columns = ['id', 'name', 'username', 'email', 'city'] 


print("--- Your Dataset is Ready ---")
print(df.head())

df.to_csv('users_for_sql.csv', index=False)
print("\nFile 'users_for_sql.csv' has been created.")