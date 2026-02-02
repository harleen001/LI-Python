import pandas as pd
df = pd.read_csv("dataset.csv")
df.head()
df.columns=df.columns.str.lower()
print(df)   # setting all column names to lowercase

#df.rename(columns={'full name':'full_name','date of birth':'date_of_birth'})   #renaming values/also a data cleaning thing
#df.columns

df.rename(columns={'full name':'full_name','date of birth':'date_of_birth'},inplace=True)    #inplace to change on same place
print(df.columns)


print(df.full_name)
df.full_name.str.split(" ")   #splitting of strings

df.full_name.str.split(" ").str.get(0)    #getting first part of the string after splitting

df['firstname'] = df.full_name.str.split(" ").str.get(0)   #getting first name from the split
print(df.firstname)

df['lastname'] = df.full_name.str.split(" ").str.get(1)   #same done with last name
print(df.lastname)  #printing last names

print(df.full_name)  #accessing full names


#using expand
df1 = df
df1.full_name.str.split(" ",expand=True)
print(df1.full_name.str.split(" ",n=1,expand=True))


df.head(3)


#---------------FINDING AND REPLACING A STRING---------------------------
print(df['income.1'])

df['income.1'].dtype   #checking data type
print(df['income.1'].str.replace("$","Euro "))    #replacing