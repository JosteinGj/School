import numpy as np
import scipy.signal as sig
import matplotlib.pyplot as plt

exp = np.exp

def forced(t):
    return 4*exp(-2*t)-3*exp(-3 * t) 


def natural(t):
    return 5*exp(-2 * t) - 4*exp(-3 * t)

def y(t):
    return forced(t)+natural(t)



x = np.linspace(0, 6, 1000)

plt.plot(x, y(x), label="total response")
plt.plot(x, forced(x), label="forced response")
plt.plot(x, natural(x), label="Natural repsonse")
plt.title("System response")
plt.xlabel("Time")
plt.ylabel("Signal")
plt.legend()
plt.savefig("signals ex 6.2 .pdf")
plt.show()

