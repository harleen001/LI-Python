import numpy as np

# intialize bytes
l = b'Harbal!'
print(type(l))

a = np.frombuffer(l, dtype = "S1")
print(a)
print(type(a))