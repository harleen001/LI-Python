import pandas as pd
df = pd.read_csv("raw_dataset.csv")

df.head()  #output of first 5 values 
df.columns #columns print
dir(df.columns) #directories of that colums

df.columns.values    #printing columns as an array

df.columns.tolist()   #get the columns as a list

df.columns.view()     #to only view the column names

#df.columns.summary()   #for a summary of column names/DEPRECEATED BY NOW

df.columns.to_series()   #CONVERTING COLUMN NAMES TO A SERIES FOR USE IN PANDAS FURTHER

df.columns.to_frame()   #CONVERTING COLUMNS TO DATA FRAMES DIRECTLY

#df.columns.contains('First Name')   #to check if column name contains 'First Name' or not

df.columns.duplicated() #returns false as most of the values are unique and not duplicate


dir(df.columns.str)  # shows attributes and methods in string


#---------------------WORKING ON DATA------------------------------
df1=df.rename(columns={'Age':'Date of Birth'})   #RENAMING COLUMN  to a different copy
#print(df1)
df.rename(columns={'Age':'Date of Birth'},inplace=True)   #on same place
print(df)


df.columns.values[7] = 'Email Address'   #renaming using selected columns
print(df)

print(df.columns)