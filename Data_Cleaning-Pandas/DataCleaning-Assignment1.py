import pandas as pd
df=pd.read_csv("dirty_cafe_sales.csv")
print("The uncleaned data is shown below")
print(df.head(10))
print("---------------------------------------------------------------------------------------------------------")

df.rename(columns={'Transaction ID':'Transaction_ID','Price Per Unit':'Price_Per_Unit','Total Spent':'Total_Spent','Payment Method':'Payment_Method','Transaction Date':'Transaction_Date'},inplace=True)    #inplace to change on same place

print("The cleaned data is as shows below")
df['Price_Per_Unit'] = "$" + df['Price_Per_Unit'].astype(str)
df= df.dropna()
df.replace("UNKNOWN", "Not Available", inplace=True)
df.replace("ERROR", "Not Available", inplace=True)


print(df.head(10))