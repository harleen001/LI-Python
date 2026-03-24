import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')
data = 'weatherAUS.csv'
df = pd.read_csv(data)
col_names = df.columns
# find categorical variables

categorical = [var for var in df.columns if df[var].dtype=='O']

print('There are {} categorical variables\n'.format(len(categorical)))

print('The categorical variables are :', categorical)
print(df[categorical].head())

# check missing values in categorical variables
df[categorical].isnull().sum()