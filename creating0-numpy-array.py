import numpy as np


arr_0d=np.array(100)
print(arr_0d)
arr_1d=np.array([1,2,3,4,5])
print(arr_1d)

arr_2d=np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr_2d)


arr_zeros=np.zeros((3,2),)
print(arr_zeros)

arr_ones=np.ones((3,2),)
print(arr_ones)


arr_identity=np.eye(3,dtype=int)   #np.identity()
print(arr_identity)