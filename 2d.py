import numpy as np
from numpy import *
from array import array
arr=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr.ndim)
print(arr.shape)
print(arr.size)
print(arr.itemsize)
print(arr.dtype)
print(arr.nbytes)
m=matrix(arr)
print(m)
d=diagonal(m)
print(d)
t=m.transpose()
print(t)
#random numbers
from numpy import *
print(random.rand(5))
print(random.rand(2,3))
print(random.randint(1,10))
print(random.randint(1,10))
