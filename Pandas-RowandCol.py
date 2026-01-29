import pandas as pd
technologies = [ ["Spark",20000, "30days"], 
                 ["pandas",20000, "40days"], 
               ]

column_names=["Courses","Fee","Duration"]
row_label=["a","b"]
df=pd.DataFrame(technologies,columns=column_names,index=row_label)
print(df)