import pandas as pd
df = pd.read_csv("raw_dataset.csv")

df.head()  #output of first 5 values 
df.columns #columns print
print(dir(df.columns)) #directories of that colums
