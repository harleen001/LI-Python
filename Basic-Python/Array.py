from array import *
vals=array('i',[1,2,3,4,5])
print(vals)
print(vals.buffer_info())

#Characters
vowels=array('u',['a','e','i','o','u'])
for e in vowels:
    print(e)

arr=array('i',[])
n=int(input("Enter length of array = "))

for i in range(n):
    x=int(input("Enter a value = "))
    arr.append(x)

print(arr)