import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from linregress import linregression

inp=np.loadtxt("data.dat")
x=inp[:,0]
y=inp[:,1]

a_0,a_1=linregression(x,y)
print(a_0,a_1)

S=sum((y-a_0-a_1*x)**2)
fig1=plt.figure()


plt.plot(x,y,".",label="y(x)")
plt.plot(x,a_0+a_1*x,label="regresjon")
plt.xlabel("x-akse")
plt.ylabel("y-akse")
plt.title("datapunkter")
plt.legend()
fig2=plt.figure()

plt.plot(x,y-a_0-a_1*x,"r",label="avvik fra regresjon")
plt.xlabel("x-akse")
plt.ylabel("y-akse")
plt.title("avvik mellom regresjon og datapunkt")
plt.legend()
plt.show()