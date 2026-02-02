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

df.head()

#finding a string expression and cleaning
print(df.salary)

print(df.salary.str.contains('19'))   #returns true and false if the string is present or not

print(df[df.salary.str.contains('19')])    #gets value of entire rows

df.salary.str.contains('19|17')    #checking for multiple expressions
df.salary.str.contains('19|17',regex=True)   #checking for multiple expressions with regular expression

df.salary.str.match('19')   #for finding exact match
print(df.quote)

df[df.quote.str.match('Operative')]   #matching exact string with this quote
print(df.salary.filter(regex='18',axis=0))   #finding this '18' with exact in index


#joining two columns
df.firstname + df.email
df.firstname +"_"+ df.email
dfall = df[['firstname','email']].apply("_".join,axis=1)
print(dfall)


#counting strings in a column
df.quote
df.quote.str.count(' ') + 1   #counting number of spaces

df.quote.str.split().str.len()   #get length of word in each row
df.quote.str.split().map(len)   #get lenght of word in each row of a column
df.quote.str.split().apply(len)


df.quote.str.split().apply(len).value_counts()    #get the total number of counts