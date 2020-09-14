import functools as ft
import scipy.integrate as scint
import numpy as np
import matplotlib.pyplot as plt


upper = 1
potname = "sin"


def V_0(x):
    return np.sin(np.pi * x)


def intfunc(x,m):
    return V_0(x) * np.sin(np.pi * x * m)


k = 50
B = [2 * scint.quad(ft.partial(intfunc, m=n), 0, 1, limit=200)[0]for n in range(1, upper+1)]
print(B)
test = np.array([[B] * k] * k).transpose()


def X(x):
    ns = np.arange(1, upper+1)
    sinxs = np.array([np.sin(np.pi * x * n) for n in ns])
    return sinxs


def Y(y):
    ns = np.arange(1, upper + 1)
    sinhys = np.array([np.sinh(np.pi * y * n) / (np.sinh(np.pi * n)) for n in ns])
    return sinhys


def potential(x,y):
    pot = np.sum((test * Y(y)) * X(x), axis=0)
    return pot


def potential_1D(x, y):
    return np.sum((np.array([B]*k).T * Y(y)) * X(x), axis=0)


# setup coordinates
x = np.linspace(0, 1, k)
y = np.linspace(0, 1, k)
xx, yy = np.meshgrid(x, y)


z = potential(xx, yy)
Ey, Ex = np.gradient(-z, x, y)

q = plt.quiver(xx, yy, Ex, Ey)


plt.contourf(xx, yy, z)
plt.colorbar()
plt.xlabel("x")
plt.ylabel("y")
plt.title("V(x, y)")
plt.savefig(f"potential contourf v0={potname} n={upper}.pdf")
plt.show()


plt.plot(x, z[-1, :])
plt.title("potential edge V(x ,1)")
plt.xlabel("x")
plt.ylabel("potential")
plt.savefig(f"v0={potname} n={upper}.pdf")
plt.show()


plt.plot(x, z[0, :])
plt.title("potential edge V(x,0)")
plt.xlabel("x")
plt.ylabel("potential")
plt.savefig(f"y0 edge v0={potname} n={upper}.pdf")
plt.show()


plt.plot(x, z[:, 0])
plt.title("potential edge V(0,y)")
plt.xlabel("y")
plt.ylabel("potential")
plt.savefig(f"x0 edge v0={potname} n={upper}.pdf")
plt.show()


plt.plot(x, z[:, -1])
plt.title("potential edge V(L,y)")
plt.xlabel("y")
plt.ylabel("potential")
plt.savefig(f"xL edge v0={potname} n={upper}.pdf")
plt.show()


plt.title("E-field")
plt.xlabel("x")
plt.ylabel("y")
plt.savefig(f"E-field v0={potname} n={upper}.pdf")
plt.show()
