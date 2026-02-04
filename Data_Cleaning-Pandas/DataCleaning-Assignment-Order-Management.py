import pandas as pd
import numpy as np
df=pd.read_csv("Order_Management_Sheet.csv")
print("---------------------------RAW DATA-----------------------------")
print(df.head())

df.dropna(subset=['Treat Disc'], inplace=True)
print("-------------------------------DATA AFTER CLEANING---------------------------------")
print(df)

