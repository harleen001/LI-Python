print(10*"harleen")
x=5
y=x*6
# print( _ +2) # _ represent output of previous operation
nums=[10,20,30]
names=["kartik","harleen"]
mix=[nums,names]  #list of lists
print(mix)

tup=(10,20,30)
print(tup[0])
# tup[0]=46   TUPLE DOESNOT SUPPORT ITEM ASSIGNMENT AS IT IS IMMUTABLE
print(tup[0])


#SET
print("Set in python")
abc={10,20,32,32,12,43,53,54,64,10}
print(abc)

#Dictionary using 2 lists
key=[1,2,3]
names=["Kartik","Harleen","Imanpal"]
dict1=dict(zip(key,names))
print(dict1)

num=6+9j
print(type(num))

print(bin(23))