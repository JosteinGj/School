import numpy as np
import matplotlib.pyplot as plt
import scipy.constants as consts




def part1_p7():
    zeta = np.linspace(0, 1, 1000000)
    mass=consts.m_e
    hbar=consts.hbar
    print(hbar,mass)
    u_0=2*1.60218e-19
    a_0 = np.sqrt(2 * mass * u_0/(hbar)**2)
    print(a_0)
    k=a_0*np.sqrt(zeta)
    alpha=a_0*np.sqrt(1-zeta)
    a=0.5e-9
    b=1.5e-9

    lhs = alpha * np.tanh(alpha*a) / k
    rhs = (np.tan(k * b) * np.sin(k * a) + np.cos(k * a)) \
          / ((-np.tan(k * b) * np.cos(k * a) + np.sin(k * a)))

    plt.plot(zeta,lhs)
    plt.plot(zeta,rhs,"r,")
    plt.ylim(-10,10)
    plt.title("boundary conditions")
    plt.xlabel("zeta")

    plt.savefig("faststoff_p5,7.png")
    plt.show()

part1_p7()

def part1_p8():
    a=0.5e-9
    b=1.5e-9
    x1=np.linspace(-b, -a, 100000)
    x2=np.linspace(-a, a, 100000)
    x3=np.linspace(a, b, 100000)
    x=np.linspace(-b, b, 100000)
    zeta = 0.14419
    print(x1[-1],x2[0])
    mass = consts.m_e
    hbar = consts.hbar

    u_0 = 2 * 1.60218e-19
    a_0 = np.sqrt(2 * mass * u_0 / (hbar) ** 2)
    k = a_0 * np.sqrt(zeta)

    alpha = a_0 * np.sqrt(1 - zeta)
    B = 1
    A = np.tan(k * b)
    C = (A * np.cos(k * a) - np.sin(k * a)) / np.cosh(alpha * a)


    psi1 = A * np.cos(k * x1) + B * np.sin(k * x1)
    psi2 = C * np.cosh(alpha * x2)
    psi3 = A * np.cos(k * x3) - B * np.sin(k * x3)

    plt.plot(x1,psi1)
    plt.plot(x2,psi2)
    plt.plot(x3,psi3)
    plt.title(r"$\psi(x)$")
    plt.xlabel("x")
    plt.ylabel(r"$\psi(x)$")
    plt.savefig("faststoff_p5,8.png")
    plt.show()
part1_p8()
