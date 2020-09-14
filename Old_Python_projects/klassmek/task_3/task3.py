import scipy.integrate as inte
import scipy.stats as stats
import numpy as np
import matplotlib.pyplot as plt
import functools as ft

OmegaD = 2/3
FD = [0, 0.5, 1.2]
q = 0.5


def physical_pendulum(t,y,F):
    if not -np.pi <= y[0] <= np.pi:
        if y[0] < 0:
            y[0] += 2*np.pi
        elif y[0] > 0:
            y[0] -= 2*np.pi
    dtheta, dw = y[1], -np.sin(y[0])-q*y[1]+F*np.sin(OmegaD*t)

    return dtheta, dw

# plot the trajectory of a driven pendulum for different driving forces
def task1():
    for FDS in FD:
        system= ft.partial(physical_pendulum,F=FDS)
        sol=inte.solve_ivp(system,y0=(0.2,0),t_span=(0,60),rtol=1e-7,atol=1e-7, vectorized=True)
        plt.plot(sol.t,sol.y[0],"r.")
        plt.show()
#task1()

# plot difference between to different initial conditions
def task2():
    x = np.linspace(0,100,100000)
    for FDS in FD[1:]:
        system = ft.partial(physical_pendulum,F=FDS)
        initialization=inte.solve_ivp(system,y0=(0.2,0),t_span=(0,300),t_eval=x, rtol=1e-7,atol=1e-7, vectorized=True)
        theta0 = initialization.y[0][-1]
        w0 = initialization.y[1][-1]
        init= np.array([theta0, w0])
        print(init)
        sol = inte.solve_ivp(system,y0=init,t_span=(0,100),t_eval=x, rtol=1e-7,atol=1e-7, vectorized=True)
        soldisplaced = inte.solve_ivp(system, y0=init+np.array([0.01,0]), t_eval=x, t_span=(0,100), rtol=1e-7, atol=1e-7, vectorized=True)
        soldiff = np.abs(sol.y[0]-soldisplaced.y[0])
        slope, intercept, rval, pval, stddev=stats.linregress(x, np.log(soldiff))

        plt.plot(sol.t, sol.y[0], "g.")
        plt.plot(soldisplaced.t, soldisplaced.y[0], "r.")
        plt.show()
        plt.plot(x, slope*x+intercept, "r")
        plt.plot(sol.t, np.log(soldiff), "b.")
        plt.show()
task2()


#stroboscopic plot of the chaotic system
def task3():
    evaluationpoints=np.arange(0,10000,2*np.pi)
    for FDS in FD[1:]:
        system = ft.partial(physical_pendulum, F=FDS)
        sol = inte.solve_ivp(system, y0=(0.2, 0), t_span=(0,10000), t_eval=evaluationpoints, rtol=1e-10, atol=1e-10, vectorized=True)
        theta, w = sol.y
        plt.plot(theta, w, "gx")
        plt.show()
#task3()









