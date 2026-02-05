import pandas as pd
account_df=pd.read_csv("account.csv")
trans_df=pd.read_csv("trans.csv")
district_df=pd.read_csv("district.csv")


dfs = [account_df,trans_df,district_df]

for i in dfs:
    print("----------------------------HEAD AND INFORMATION------------------")
    print(i.head())   #Head and Info for all dataframes
    print(i.info())
    
    print("------------------------UNIQUE VALUES------------------------------")
    print(i.nunique())  #Unique Values for all dataframes

    print("----------------------DUPLICATE VALUES----------------------------")
    print(i.duplicated().sum()) #duplicate sum




account_df['account_open_date'] = pd.to_datetime(account_df['account_open_date'])   #datatype changed with todatetime
trans_df['date'] = pd.to_datetime(trans_df['date'])

 