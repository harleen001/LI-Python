import pandas as pd
df = pd.read_csv("raw_dataset.csv")

df.head()  #output of first 5 values 
df.columns #columns print
dir(df.columns) #directories of that colums

df.columns.values    #printing columns as an array

df.columns.tolist()   #get the columns as a list

df.columns.view()     #to only view the column names

df.columns.summary()   #for a summary of column names/DEPRECEATED BY NOW

df.columns.to_series()   #CONVERTING COLUMN NAMES TO A SERIES FOR USE IN PANDAS FURTHER