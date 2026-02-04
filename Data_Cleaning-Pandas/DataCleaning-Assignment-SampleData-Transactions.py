import pandas as pd
import numpy as np
df=pd.read_csv("Transactions.csv")
print("---------------------------RAW DATA-----------------------------")
print(df.head())


df.rename(columns = {'transaction_id':'Transaction_Id'},inplace=True)
df.rename(columns = {'currency_type':'Currency_Type'},inplace=True)
df.rename(columns = {'usd_value':'USD_Value'},inplace=True) 
df.rename(columns = {'deposited_date':'Deposited_Date'},inplace=True)
df.rename(columns = {'deposited_time':'Deposited_Time'},inplace=True)
df.rename(columns = {'user_id':'User_Id'},inplace=True)


df= df.dropna()

column_order = ['User_Id', 'Transaction_Id', 'Currency_Type', 'USD_Value', 'Deposited_Date', 'Deposited_Time']
df = df[column_order]
df['USD_Value'] = "$" + df['USD_Value'].astype(str)

print("-------------------------------DATA AFTER CLEANING---------------------------------")
print(df.head())
