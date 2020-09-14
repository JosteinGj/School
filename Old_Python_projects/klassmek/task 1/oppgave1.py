import scipy.integrate as sci
import numpy as np
import matplotlib.pyplot as plt

length=1
def anal_pendulum(theta,w,h):
    dtheta=theta + h*w
    dw=w-(9.81*h*np.sin(theta))
    denergy=(0.2*w**2/2+0.2*9.81*(1-np.cos(theta)))*h**2
    return dtheta,dw, denergy
def anal_runke_gutta(t,y):
    dtheta= y[1]
    dw=-9.81*y[0]
    return dtheta,dw
def runke_gutta_anal_energy(t,y):
    return((0.2*(y[1])**2)/2 + 0.2 * 9.81* ( 1-np.cos(y[0]) ))

def shady_pendulum(theta,w,h):
    dtheta=theta +h*w
    dw=w-(9.81*h*theta)
    denergy = (0.2*(w**2 + 9.81 * theta**2) * h** 2) / 2
    return dtheta,dw,denergy


def runke_gutta(f,energ,x0,w0):
    sol=sci.solve_ivp(f,y0=(x0,w0),t_span=(0,10),evaltimes=np.linspace(0,10,1000),vectorized=True)
    energy= sci.solve_ivp(energ,y0=(x0,w0),t_span=(0,10),evaltimes=np.linspace(0,10,1000))
    plt.plot(np.linspace(0,10,1000),sol[0])
    plt.xlabel(f"runke gutta pendulum")
    plt.show()
    plt.plot(np.linspace(0,10,1000),energy)
    plt.show()
    return sol,energy
#simple eulers method on function f starting at x0 with n steps of length h
def eulercromer(f,x0,w0,h,n):
    sol=[[x0],[w0]]
    energy=[f(x0,w0,h)[2]]
    time=[0]
    for i in range(n):
        sol[1].append(f(sol[0][-1], sol[1][-1], h)[1])
        sol[0].append(f(sol[0][-1],sol[1][-1],h)[0])
        energy.append(f(sol[0][-1], sol[1][-1], h)[2] + energy[-1])
        time.append(h*(i+1))

    plt.plot(time,sol[0])
    plt.xlabel(f"{f} eulercormer")
    plt.show()
    plt.plot(time,energy)
    plt.xlabel((f"{f} energy  euler cromer"))

    plt.show()
    return sol,energy,time
def euler(f,x0,w0,h,n):
    sol = [[x0], [w0]]
    energy = [f(x0, w0, h)[2]]
    time = [0]
    for i in range(n):
        sol[1].append(f(sol[0][-1], sol[1][-1], h)[1])
        sol[0].append(f(sol[0][-1], sol[1][-2], h)[0])
        energy.append(f(sol[0][-1], sol[1][-1], h)[2] + energy[-1])
        time.append(h * (i + 1))

    plt.plot(time, sol[0])
    plt.xlabel(f"{f} simple euler")
    plt.show()
    plt.plot(time, energy)
    plt.xlabel((f"{f} energy simple euler"))
    plt.show()
    return sol, energy, time

print(runke_gutta(anal_runke_gutta,runke_gutta_anal_energy,0.2,0))
print(euler(shady_pendulum,0.2,0,0.01,1000))
print(euler(anal_pendulum,0.2,0,0.01,1000))
print(eulercromer(shady_pendulum,0.2,0,0.01,1000))
print(eulercromer(anal_pendulum,0.2,0,0.01,1000))



