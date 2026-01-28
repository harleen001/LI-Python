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
print("-----------------------------------------------------------")
print(df[df["Ename"].str.startswith('P')])

print("-----------------------------------------------------------")
print(df[df["Ename"].str.endswith('y')])

print("-----------------------------------------------------------")
print(df.query('Ename.str.len()==5'))

print("-----------------------------------------------------------")
print(df[(df["Job"].str.startswith('m')) & (df["Job"].str[-2]=='e')])

print("-----------------------------------------------------------")
print(df[(df["Ename"].str[1]=='l') & (df["Ename"].str[-1]=='e')])

print("-----------------------------------------------------------")
print(df[(df["Ename"].str[2]=='r')]) #specific character search from index

print("-----------------------------------------------------------")
print(df[(df["salary"]>=45000) & (df["salary"]<=55000)])