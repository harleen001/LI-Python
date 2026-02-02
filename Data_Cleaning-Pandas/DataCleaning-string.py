import pandas as pd
df = pd.read_csv("dataset.csv")
df.head()
df.columns=df.columns.str.lower()
print(df)   # setting all column names to lowercase

#df.rename(columns={'full name':'full_name','date of birth':'date_of_birth'})   #renaming values/also a data cleaning thing
#df.columns

df.rename(columns={'full name':'full_name','date of birth':'date_of_birth'},inplace=True)    #inplace to change on same place
print(df.columns)


print(df.full_name)