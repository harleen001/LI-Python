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



#Converting to uppercase
district_df['region']=district_df['region'].str.upper()
district_df['district_name']=district_df['district_name'].str.upper()



#Checking for missing values
print("Account Missing Data",account_df.isna().sum())
print("District Missing Data",district_df.isna().sum())
 
#Fill missing values with the median of each column / IMPUTATION
#Missing columns filled
impute_cols = ['population', 'average_salary', 'unemployment_rate', 'num_committed_crimes']
district_df[impute_cols] = district_df[impute_cols].fillna(district_df[impute_cols].median())
print("District Missing Data",district_df.isna().sum())


print("Trans Missing Data",trans_df.isna().sum())



#Divide the columns into numeric columns and categorical columns, then use the fillna method to fill numeric columns with -999, fill categorical columns with 'UNKNOWN'
numeric_cols = trans_df.select_dtypes(include=['number']).columns
categorical_cols = trans_df.select_dtypes(exclude=['number']).columns

trans_df[numeric_cols] = trans_df[numeric_cols].fillna(-999) #Fill numeric columns with -999
trans_df[categorical_cols] = trans_df[categorical_cols].fillna('UNKNOWN') #Fill categorical columns with 'UNKNOWN'


print(district_df.describe())

print("----------------------------------------LEFT JOIN----------------------------------------")
account_district = pd.merge(account_df, district_df, on='district_id', how='left')
print(account_district)



print("-----------------------------ACCOUNT INFORMATON AND MISSING VALUE SUM------------------------------")
print(account_district.info())
print(account_district.isna().sum())




print("-------------------------LEFT JOIN AND NEW ALL DATA ASSIGNED-----------------------------------")
all_data = pd.merge(trans_df, account_district, on='account_id', how='left')
all_data.info()
print(all_data.isna().sum())
print(all_data.head())





all_data['account_open_year'] = all_data['account_open_date'].dt.year
print(all_data[['account_open_date', 'account_open_year']].head())
#adding new column of account open year


print("-------------------------------PRINTING OUTPUT DATA--------------------------------------------")
for i in dfs:
    print(i.head())