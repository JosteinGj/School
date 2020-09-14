# Signals analysis exercise 1


import matplotlib.pyplot as plt
import numpy as np
import scipy.signal as sig
# task  2.1 a-ii


def f(x):
    return np.heaviside(x+3,1) +(x/3)*np.heaviside(x,1)-(x/3+1)*np.heaviside(x-3,1) 

def plot21ii():
    interval = np.linspace(-5, 5, 1000)
    xs = 3 * interval - 6
    print(xs)
    vals = list(map(f, xs))
    plt.plot(interval, vals, label="Transformed Signal")
    plt.legend()
    plt.savefig("Task2,1 a-ii.pdf")
    plt.show()


#plot21ii()


# task 2.1 b-iv


def g(x):
    return (2*x/3)*np.heaviside(x,1)-(2*x/3-2)*np.heaviside(x-3,1)+(2*x/3-8)*np.heaviside(x-6,1)-(2*x/3-6)*np.heaviside(x-9,1)

def plot21biv():
    interval = np.linspace(-15, 15, 100)
    xs =  (-1)*interval+2
    plt.plot(interval, list(map(g, xs)), label="Transformed Signal")
    plt.legend()
    plt.savefig("Task2,1 b-vi.pdf")
    plt.show()


#plot21biv()


# task 2.5 a


def h(x):
    return (-3*x/5 + 4/5) * np.heaviside(x+2,1) +(x + 3*x/5 - 5 + 1/5)*np.heaviside(x-3,1)+(-x+4)*np.heaviside(x-4,1)
#plt.plot(np.linspace(-5,5,1000),h(np.linspace(-5,5,1000)))
#plt.show()


def heven(x):
    return 4/5*np.heaviside(x+2,1)-24/5*np.heaviside(x-3,1)+4*np.heaviside( x- 4, 1)


def hodd(x):
    return -3*x/5*np.heaviside(x+2, 1)+8*x/5*np.heaviside(x-3 ,1)-x*np.heaviside(x - 4,1)


def evenOddplot(f, x):
    plt.plot(x, heven(x), label="evencomp")
    plt.plot(x, hodd(x), label="oddcomp")
    plt.plot(x,heven(x)+hodd(x),label="oddcomp+evencomp")
    plt.legend()
    plt.savefig("oddeven.pdf")
    plt.show()


evenOddplot(h, np.linspace(-3, 5, 1000))


# task 2.6
# x(t) = -2t ; x(-t) = 2t = -x(t) Odd
# x(t) = exp(-|4t|) ; x(-t) = exp(-|-4t|) = x(t) Even
# x(t) = 5cos(6t) ; x(-t) = 5cos(-6t) = x(t) Even
# x(t) = u(-t) - u(t) = 1 if x < 0 -1 else ; x(-t) = u(t) - u(-t) = -x(t)  Odd
# x(t) = sin(6t-pi/2) sin is know odd
# x(t) = u(-t) + u(t) = 1 Even'


def u(t):
    if t > 0:
        return 1
    else:
        return 0
def task26(t):
    return 3*t*np.heaviside(t,1)-(3*t-3)*np.heaviside(t-1,1)+(-3*t+6)*np.heaviside(t-2,1)+(3*t-9)*np.heaviside(t-3,1)
x=np.linspace(-3,5,1000)
plt.plot(x,task26(x))
plt.show()
def x223(t):
    if t<0:
        return 0
    elif 0 <= t < 1:
        return 3+t
    elif 1 <= t < 2:
        return 4
    elif 2 <= t <= 3:
        return -1


def plot223():
    time = np.linspace(-1, 5, 10000)
    x = np.array(list(map(x223, time)))
    plt.plot(time, x, label="plot of signal in 2.23")
    plt.legend()
    plt.savefig("Task_223.pdf")
    plt.show()


#plot223()


def rektpuls(amp, width):
    t = np.linspace(-width, width, 10000)
    ls = np.array(list(map(u, -t + width / 2)))
    rs = np.array(list(map(u, t + width / 2)))
    pulse = amp * ls * rs
    plt.plot(t, pulse, label="Signal")
    plt.savefig("rectpulse.pdf")
    plt.show()


#rektpuls(1, 0.01)


def tripuls(amp, width):
    t = np.linspace(0, width, 1000)
    pulse = amp * sig.sawtooth((2 * np.pi) / width * t, 0.5)
    plt.plot(t, pulse, label="trianle pulse")
    plt.legend()
    plt.savefig("tripulse.pdf")
    plt.show()


#tripuls(2, 0.005)


def gaussianplot(amp, width):
    t = np.linspace(-2, 2, 10000)
    x = amp * np.exp(-(t / width) ** 2 / 2)
    plt.plot(t, x, label = "gaussian")
    plt.legend()
    plt.savefig("gaussian.pdf")
    plt.show()


# gaussianplot(7,1/np.e)


def rectwave(pulsewidth, separation, numOfwaves):
    t = np.linspace(-(pulsewidth + separation) * (numOfwaves + 0.1)/2, (pulsewidth + separation) * (numOfwaves + 0.1)/2, 100000)
    dutycycle = pulsewidth/(pulsewidth+separation)
    signal = sig.square(2 * np.pi * 1 / (pulsewidth + separation) * t,
            dutycycle) / 2 + 1 / 2
    plt.plot(t, signal, label="rectangular wave")
    plt.legend()
    plt.savefig("rectangleWave.pdf")
    plt.show()


rectwave(0.002,0.01,11)

def test(t):
    return 1-(t+1)*np.heaviside(t+1,1) +3*(t-1)*np.heaviside(t-1,1) - 2*(t-2)*np.heaviside(t-2,1)
x=np.linspace(-3,3,100)
plt.plot(x,test(x))
plt.show()
