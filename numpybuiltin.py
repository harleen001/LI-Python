import numpy as np

arr=np.array([1,2,3,4,5])
print(arr.ndim)     #dimension  1d/2d/3d
print(arr.shape)    #shape according to values
print(arr.size)     #no. of values
print(arr.dtype)    #datatype
print(arr.itemsize) #each value size
print(arr.strides)  #next item at how many bytes difference
print(arr.nbytes)   #5*8=40 total memory
print(arr.data)     #memory location of the array
print(arr.flags)    #all boolean properties of the array like c contigious and f contgioues for col and row and so on
