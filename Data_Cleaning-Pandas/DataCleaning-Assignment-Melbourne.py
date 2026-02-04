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

print("---------------------------------------------------------")
checksum=data.isnull().all(axis=1).sum()   #checking sum of all null values which results to 0
print(checksum)

len(data)  #length of data

#amount of percentage of missing values

#percentage_of_missing_values=
data.isnull().sum(axis=0).sort_values(ascending=False)/len(data)*100

#print(percentage_of_missing_values)

#selecting top 3 null value percentage
Col = data.isnull().sum(axis=0).sort_values(ascending=False).head(3).index.values
print(Col)
data = data.drop(Col,axis='columns')
print(data)


data.isnull().sum().sort_values(ascending=False)/len(data)*100   #again values checked

print("-----------------------------------------------------------------------------")
data[data.isnull().sum(axis=1) > 5]

len(data[data.isnull().sum(axis=1) > 5])  #length checked
data[data.isnull().sum(axis=1) > 5].shape  #shape checked

len(data[data.isnull().sum(axis=1) > 5])/len(data)*100 #percentage checked
round(len(data[data.isnull().sum(axis=1) > 5])/len(data)*100,2)  #percentage rounded off to two places


data = data[data.isnull().sum(axis=1) <=5]   #rows less than 5 not assigned retained
print(data) 


data.isnull().sum().sort_values(ascending=False)/len(data)*100    #percentage of missing values for each column

#removing NAN Values
print("------------------------------------------------------------------------------------------")
data = data[data.Price.notnull()]
print(data)


notassignedcheck=round(data.isnull().sum().sort_values(ascending=False)/len(data)*100,2)  #percentage of missing values and round off result to 2 places
print(notassignedcheck)



print(data['Landsize'].describe())  #describing row of LANDSLIDE Column which has 9.83% not assigned data

data = data[data.Landsize.notnull()]     #shows data where landslide is not null
print(data)


round(data.isnull().sum().sort_values(ascending=False)/len(data)*100,2)   #AGAIN ROUNDOFF BY 2 DECIMAL PLACES

#describing latitute and longitude and then putting values by mean
data.loc[:,['Lattitude','Longtitude']].describe()
data['Lattitude'].mean()

data.loc[:,'Lattitude'].fillna(data['Lattitude'].mean(),inplace=True)
data.loc[:,'Longtitude'].fillna(data['Longtitude'].mean(),inplace=True)
print("-------------------------LATITUDE AND LONGITUDE INSERTED----------------------------------")
print(data)