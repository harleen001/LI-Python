import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
df = pd.read_csv("heart.csv")

# Rename columns
to_rename = {
    'age' : 'Age','sex' : 'Sex','cp' : 'Chest Pain','trestbps' : 'BPS','chol' : 'Cholesterol',
    'fbs' : 'FBS','restecg' : 'RestECG','thalach' : 'Thalach','exang' : 'EIA','oldpeak' : 'Oldpeak',
    'slope' : 'Slope','ca' : 'CA','thal' : 'Thal','target' : 'Target'
}
df.rename(columns = to_rename, inplace = True)

# Fix 1: Use specific figures or plt.show() to prevent plots from overlapping/not showing
plt.figure(figsize=(10, 5))
sns.countplot(x='Age', data=df)

plt.figure(figsize=(10, 5))
sns.countplot(x='Sex', data=df)

plt.figure(figsize=(10, 5))
sns.countplot(x='Chest Pain', data=df)

# Fix 2: Explicitly pass the x variable for the countplot to avoid future errors
plt.figure(figsize=(10, 5))
sns.countplot(x='BPS', data=df)

# Fix 3: replace distplot (deprecated) with histplot or displot
plt.figure(figsize=(10, 5))
sns.histplot(df["Cholesterol"], color='c', kde=True) 

# Fix 4: sns.countplot requires the 'x' argument explicitly named for the Series
plt.figure(figsize=(10, 5))
sns.countplot(x='FBS', data=df)

# Fix 5: Jointplot works fine, but good to ensure plt.show() is called at the end
sns.jointplot(x='Thalach', y='Oldpeak', data=df, kind='hex')




df1 = df[['Sex','BPS','Cholesterol','Thalach', 'Oldpeak']]
g = sns.pairplot(df1, hue='Sex')



plt.show()