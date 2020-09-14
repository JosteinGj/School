import scipy as sci
import numpy as np


def mylu(arr):
    n=len(arr[0])
    P= np.array([i for i in range(n)])
    print("P",P)
    print(arr)
    transp=arr.transpose()

    for k in range(n):
        colmax=np.max(np.abs(transp[k]))
        print("colmax",colmax)
        for j in range(k,n):
            print("k:", k, " j:", j, " ", transp[k][j])
            if transp[k][j]==colmax:
                temp=P[j]
                P[j]=P[k]
                P[k]=temp

    print(P)
    print(arr)
    for k in range(n):
        for j in range(k+1,n):
            # print(arr)
            arr[P[j]][k] = arr[P[j]][k]/arr[P[k]][k]
            for i in range(k+1,n):
                arr[P[j]][i]= arr[P[j]][i]-arr[P[j]][k]*arr[P[k]][i]
    print(arr)
    print(P)
    return P, arr



a=np.array([[1,2,3,4],[5,6,7,8],[2,4,6,8],[1,3,5,7]])
mylu(a)



