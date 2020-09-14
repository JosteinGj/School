import numpy as np
import matplotlib.pyplot as plt

N=330
I=1
mu_0=4*np.pi*10**-7
R=0.07
x0=0.4


def B_felt_kort_spole(x):
    prefactor=(N * I * mu_0) / (2 * R)
    return prefactor * (1 + (x / R) ** 2) ** (-1.5)*10**4
def main():
    filnavn="kortspole.csv"
    data=np.loadtxt("kortspole.csv",delimiter=",")
    x=data[ : ,0]
    B2=data[: ,1]
    B1=B_felt_kort_spole(x-x0)
    print (x-x0)
    print(B1)
    plt.plot(x-x0,B1,"o",label="Beregnet")
    plt.plot(x-x0,B2,label="målt")
    plt.xlabel("avstand fra senter av spolen [cm]")
    plt.ylabel("magnetfelt [gauss]")
    plt.legend()
    plt.show()
main()
