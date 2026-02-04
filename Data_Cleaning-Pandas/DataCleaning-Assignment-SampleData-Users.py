import pandas as pd
import numpy as np
df=pd.read_csv("Users.csv")
print("---------------------------RAW DATA-----------------------------")
print(df.head())

df.rename(columns = {'user_id':'User_Id'},inplace=True)
df.rename(columns = {'name':'Name'},inplace=True)
df.rename(columns = {'email':'Email'},inplace=True)
df.rename(columns = {'country':'Country'},inplace=True) 
df.rename(columns = {'registered_date':'Registered_Date'},inplace=True)
df.rename(columns = {'registered_time':'Registered_Time'},inplace=True)


df['First_Name']=df['Name'].str.split(" ").str.get(0)
df['Last_Name']=df['Name'].str.split(" ").str.get(1)

del df['Name']

df= df.dropna()

column_order = ['User_Id', 'First_Name', 'Last_Name', 'Email', 'Country', 'Registered_Date', 'Registered_Time']
df = df[column_order]


print("-------------------------------DATA AFTER CLEANING---------------------------------")
print(df.head())
