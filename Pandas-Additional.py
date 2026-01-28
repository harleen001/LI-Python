import pandas as pd
pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)
d={'empid':pd.Series([1001,1002,1003,1004,1005,1006,1007,1008,1009,1010],index=[1,2,3,4,5,6,7,8,9,10]),
   'Ename':pd.Series(['Smith','Blake','King','Harry','Mohit','Harry','Pawan','perry','jerry','gagan'],
                     index=[1,2,3,4,5,6,7,8,9,10]),
   'Job':pd.Series(['manager','salesmen','president','clerk','programmer','clerk','programmer','clerk','manager','salesmen',],
                   index=[1,2,3,4,5,6,7,8,9,10]),
   'salary':pd.Series([55000,65000,85000,25000,55000,25000,65000,25000,35000,45000],index=[1,2,3,4,5,6,7,8,9,10]),
   'comm':pd.Series([100,200,100,500,300,500],index=[1,3,5,7,9,10]),'Deptno':pd.Series([10,20,10,10,30,10,20,10,30,40],index=[1,2,3,4,5,6,7,8,9,10])}
df=pd.DataFrame(d)
df
print("--------------------------------------------------------------")
print(df[(df["salary"]!=45000) & (df["salary"]!=55000)] )   # shows data which is not present in it

print("--------------------------------------------------------------")
print(df.count())   #count the values 

print("--------------------------------------------------------------")
print(df.value_counts(df["Job"]))  #value counts of all type jobs

print("--------------------------------------------------------------")
print(df.value_counts(df["Job"]=='manager'))  #value count if manager job is true or false for how many values

print("---------------------------------------------")
sal=df["salary"]   #prints out the max salary by taking it
max_sal=sal.max()   #max here
print(max_sal)

print("-----------------------------------------------------------------------------------")
#whole row printed of maximum salary
sal=df["salary"]
max_sal=sal.max()
result=df[df["salary"]==max_sal]
print(result)


print("-----------------------------------------------------------------------------------")
#only given columns of maximum salary
sal=df["salary"]
max_sal=sal.max()
result=df[df["salary"]==max_sal][["Ename","salary","Deptno","Job"]]
print(result)

print("---------------------------------------------------------------------")
#shows if values are nulll or not
result=df['comm'].isnull().values.any()
print(result)


print("---------------------------------------------------------")
#checks for each column if it is null or not
result=df['comm'].isnull()
print(result)

print("------------------------------------------------------------")
#for specific values not present in it
result=df[(df["comm"]!=200.0) & (df["comm"]!=500.0)]
print(result)