import random

def func(a):
    b=[0]*len(a)
    for c in range(len(a)):
        d=random.randint(0,len(a)-1)
        b[c]=a[d]
        del a[d]
    return b
print(func([1,2,3,4,5,6,7,8,9,10]))
