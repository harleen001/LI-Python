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


# print categorical variables containing missing values

cat1 = [var for var in categorical if df[var].isnull().sum()!=0]

print(df[cat1].isnull().sum())

# view frequency of categorical variables

for var in categorical:

    print(df[var].value_counts())

# view frequency distribution of categorical variables
import numpy as np
for var in categorical:

    print(df[var].value_counts()/np.float64(len(df)))