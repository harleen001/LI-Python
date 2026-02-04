import pandas as pd
import numpy as np
df=pd.read_csv("Bets.csv")
print("---------------------------RAW DATA-----------------------------")
print(df.head())


df.rename(columns = {'bet_id':'Bet_Id'},inplace=True)
df.rename(columns = {'created_at':'Created_At'},inplace=True)
df.rename(columns = {'turnover':'Turnover'},inplace=True) 
df.rename(columns = {'payout_multiplier':'Payout_Multiplier'},inplace=True)
df.rename(columns = {'user_id':'User_Id'},inplace=True)
df.rename(columns = {'game_name':'Game_Name'},inplace=True)


df['Date_Created']=df['Created_At'].str.split(" ").str.get(0)
df['Time_Created']=df['Created_At'].str.split(" ").str.get(1)

del df['Created_At']

df= df.dropna()

df['Turnover'] = "$" + df['Turnover'].astype(str)


df.replace(0, np.nan, inplace=True)

df.dropna(inplace=True)

print("-------------------------------DATA AFTER CLEANING---------------------------------")
print(df.head())
