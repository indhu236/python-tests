def square(n):
    return n*n
lst=[2,4,6,8]
list1=map(square,lst)
for ele in list1:
    print(ele,end='')
