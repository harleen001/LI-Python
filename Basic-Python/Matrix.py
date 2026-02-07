from numpy import *
arr1= array([
        [1,2,3,6,2,9],
        [4,5,6,7,5,3]
])
print(arr1)
print(arr1.dtype) #datatype
print(arr1.ndim) #dimension
print(arr1.shape) #no of rows and cols

arr2=arr1.flatten()  #flatten from 2d/3d to 1d
print(arr2)

#reshape is reverse like flat to 2d/3d array

arr3=arr1.reshape(3,4) #(2,2,3)---> two 2 dimensional array
print(arr3)


m=matrix(arr1) #simply making matrix out of array, with 'm' you can perform more matrices operations

mx=matrix('1 2 3 ; 4 5 6 ; 7 8 9')
print(mx)
print(diagonal(mx)) #diagonal for that matrix
print(mx.min())
print(mx.max())