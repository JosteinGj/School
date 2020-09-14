import numpy as np
import operator as op
matrix=np.loadtxt("euler 1.txt",dtype=int)
maks=0
for row in range(17):
    for i in range(17):
        if row > 17:
            prod1 = matrix[row][i] * matrix[row][i + 1] * matrix[row][i + 2] * matrix[row][i + 3]
            if max(plist) > maks:
                maks = max(plist)
        elif row<=17:
            prod1=matrix[row][i]*matrix[row][i+1]*matrix[row][i+2]*matrix[row][i+3]
            prod2=matrix[row][i]*matrix[row+1][i+1]*matrix[row+2][i+2]*matrix[row+3][i+3]
            prod3=matrix[row][i]*matrix[row+1][i]*matrix[row+2][i]*matrix[row+3][i]
            plist=[prod1,prod2,prod3]
            if max(plist)>maks:
                maks=max(plist)


print(maks)
print(matrix)
