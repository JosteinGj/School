import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axis3d
from matplotlib import cm
x=np.linspace(-2,2,50)
y=np.linspace(-2,2,50)
x,y=np.meshgrid(x,y)
E=1/(x**2+y**2)
U=1/np.sqrt(x**2+y**2)
fig=plt.figure()
ax=fig.add_subplot(121,projection="3d")
ax.plot_surface(x,y,E)
ax.plot_surface(x,y,E,cmap=cm.coolwarm)
ax2=fig.add_subplot(122,projection="3d")
surf=ax2.plot_surface(x,y,U,cmap=cm.seismic)
fig.colorbar(surf)
plt.show()
