import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

def linregression(x,y):
    sx=np.sum(x)
    sy=np.sum(y)
    sxy=np.dot(x,y)
    sxx=np.dot(x,x)
    N=len(x)
    Delta=N*sxx-sx**2
    a_0=(sy*sxx-sx*sxy)/Delta
    a_1=(N*sxy-sx*sy)/Delta
    S=sum((y-a_0-a_1*x)**2)
    da_0=np.sqrt((S*sxx)/((N-2)*Delta))
    da_1=np.sqrt(N*S/((N-2)*Delta))
    print("a\u2080={}, a\u2081={}, \u0394a\u2080={}, \u0394a\u2081={}".format(a_0,a_1,da_0,da_1))
    return a_0, a_1,
