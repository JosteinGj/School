import numpy as np
import matplotlib.pyplot as plt
from linregress import linregression

inp=np.loadtxt("sinus.dat")
theta=inp[:,0]
y=inp[:,1]

sintheta=np.sin(theta)
thetaFit=np.linspace(min(theta),max(theta),200)
thetafitsin=np.sin(thetaFit)

a_0,a_1=linregression(sintheta,y)
ythetafit=(a_0+a_1*np.sin(thetaFit))

fig1=plt.figure()
plt.subplots_adjust(hspace=0.5)

plt.plot(theta,y,"g.",label="y(theta)")
plt.plot(thetaFit,ythetafit,label="regresjon av thetafit")
#ax1.plot(theta,a_0+a_1*theta)
plt.title("sinus regresjon")
plt.xlabel("x-akse")
plt.ylabel("y-akse")
plt.legend(bbox_to_anchor=[0.6, 1],loc="best")
fig2=plt.figure()

plt.plot(sintheta,y,"b.",label="y(sin(theta))")
plt.plot(sintheta,a_0+a_1*sintheta,label="linregresjon av mhp sintheta")
#ax2.plot(x,y-a_0-a_1*x,"r.")
plt.xlabel("x-akse")
plt.ylabel("y-akse")
plt.legend(bbox_to_anchor=[0.6, 1],loc="best")
plt.show()