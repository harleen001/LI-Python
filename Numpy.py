from numpy import *

arr = array([[1, 2, 3],
             [2, 5, 6]])

print(arr)


A=linspace(0,15,20) #breaking into 20 parts
print(A)

B=arange(1,10,2)
print(B)       
# zeros(5) and ones(5)


arr1=array([1,2,3,4,5])
arr2=array([1,2,3,4,5])
arr3=arr1+arr2
print(arr3) #Vectorized operation in an array