import numpy as np
a = np.array([[11,2,23],[33,44,5],[84,25,16]])

print ("The array is :")
print (a )
print ('\n')

#To return array of items in the second column
print ('The items in the second column are:')
print (a[..., 1] )
print ('\n')

# In order to slice all items from the second row
print ('The items in the second row are:')
print (a[1, ...])
print ('\n')

# In order to slice all items from column 1 onwards
print ('The items onwards to column 1 are:' )
print (a[..., 1:])