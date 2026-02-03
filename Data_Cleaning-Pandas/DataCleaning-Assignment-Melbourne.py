import pandas as pd
data = pd.read_csv('Melbourne.csv')
OrgData = data
print(data)

print(data.shape) #checking shape of data
print(data.info())  # shows information of data



# cleaning the data
print(data.isnull().sum(axis=0).sort_values(ascending=False)) #checking null values

print(data.isnull().sum(axis=1).sort_values(ascending=False))  #rowwise null count


print(data.isnull().sum() >0)  #FIND COLUMN HAVING ATLEAST ONE NULL value, returns as true/false

d = data.isnull().any()
print(d) #columms having at least one missing value


d.index[d.values]

data.isnull().any(axis=0) #any operates on columns by default

data.isnull().any(axis=1)  #check missing value row wise

data[data.isnull().any(axis=1)]


data.isnull().all(axis=0)  #columns having all missing values
data.isnull().all(axis=1)  # rows having all missing values