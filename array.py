from array import *
x=array('i',[10,20,30,40,50])
n=len(x)
for i in range(n):
    print(x[i],end='')
for ele in x:
    print(ele,end='')
y=x[1:4]
print(y)
#array in numpy
import numpy
arr=numpy.array([10,20,30,40,50])
for ele in arr:
    print(ele,end='')

