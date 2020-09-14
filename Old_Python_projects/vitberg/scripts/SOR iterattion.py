import numpy as np
import scipy.sparse as spar

diagons=[[-1]*8,[2]*10,[-1]*8]

A=spar.diags(diagons,[-1,0,1]).toarray()
print(A)
def err(u,v,tol):
    if np.linalg.norm(u-v)<=tol:
        return True
    else: return False

def SOR(A,f=0,w=1):
    L=np.diag(-1,-1)
    U=np.diag(-1,1)
    D=np.diag(2)
    print(L,U,D)


    x_0=np.zeros(10)
    x_old=x_0
    counter=0
    while counter<1000 :
        return 0

SOR(A)