import pandas as pd

# Try default first
try:
    df = pd.read_csv("unclean_data.csv")
except UnicodeDecodeError:
    # fallback to latin1
    df = pd.read_csv("unclean_data.csv", encoding='latin1')

print(df.head())

df.columns
df.columns.str.upper()

df.columns
df.columns = df.columns.str.upper()

df.columns

df.rename(columns = {'DURATION':'TIME'})  #renaming columns

df.isnull()   #checking null value

df.isnull().any()   #boolean check for null values return as true/false
df.isnull().any()

df.isnull().sum()

df_with_0 = df.fillna(0)  #filling not assigned values with 0
df_with_0.head()


#filling values with mean
df['DURATION'].mean()
df_with_mean = df.DURATION.fillna(df['DURATION'].mean())
print(df_with_mean)

df.shape  #checking shape
df_drop = df.dropna()  #dropping not assigned values

df_drop.shape  #shape again checked
df.shape
print(df_drop.head()) #checked
