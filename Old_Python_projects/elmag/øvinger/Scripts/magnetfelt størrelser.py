import numpy as np
import matplotlib.pyplot as plt
import scipy.constants as const

n=330
mu=const.mu_0
i=0.75
l=0.035
r=0.063
x=l/2
prefac=(*mu*i*10**4)/(2*l)
output=0
for lag in range(0,20):
    print(lag)
    a1=x/np.sqrt(x**2+(r+0.0007*lag)**2)
    a2=-(l-x)/np.sqrt((l-x)**2+(r+0.0007*lag)**2)
    b=prefac*(a1-a2)
    output+=b
print(output)