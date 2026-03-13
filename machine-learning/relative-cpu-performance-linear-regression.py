import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

warnings.filterwarnings('ignore')
filename = "machine-test.csv"

df = pd.read_csv(filename, header = None)

print("Shape of dataframe df: {}".format(df.shape))
col_names = ['Vendor Name','Model Name', 'MYCT', 'MMIN', 'MMAX', 'CACH','CHMIN', 'CHMAX', 'PRP', 'ERP' ]
df.columns = col_names

#finding categorical variables and searching them
categorical = [col for col in df.columns if df[col].dtype=='O']
print('There are {} categorical variables'.format(len(categorical)))

print(categorical)


df['Vendor Name'].value_counts()
print('Number of unique Model Names: ', len(df['Model Name'].unique()))
print('Number  of instances of models: ', len(df))


#finding numerical variables and searching them
numerical = [col for col in df.columns if df[col].dtype!='O']
print('There are {} numerical variables'.format(len(numerical)))
print(numerical)