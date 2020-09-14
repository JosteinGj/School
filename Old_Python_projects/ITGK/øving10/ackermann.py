import sys
sys.setrecursionlimit(15000)
def ackermann(x,y):
    if x==0:
        return y+1
    if y==0:
        return ackermann(x-1,1)
    else:
        return ackermann(x-1,ackermann(x,y-1))



print(ackermann(4,1))