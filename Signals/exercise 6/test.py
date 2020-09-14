import scipy.signal as sig
import numpy as np
import matplotlib.pyplot as plt

r1 = 10
r2 = 10
l1 = 100e-3
l2 = 100e-3
c = 10e-6
A = np.array(((-r1 / l1, 0, -1 / l1), (0, -r2 / l2, -1. / l1), (1 / c, 1 / c, 0)))

sys = sig.StateSpace(A, np.reshape(np.array([1/l1, 0, 0]), (3, 1)), np.array([0, -r2, 0]), 0)

impTime, impulseResponse = sig.impulse(sys, N=10000)


plt.plot(impTime, impulseResponse, label="Impulse response")
plt.xlabel("time")
plt.ylabel("signal")
plt.legend()
plt.plot()

stepTime, stepResponse = sig.step(sys, N=10000)
plt.plot(stepTime, stepResponse, label="Step response")
plt.xlabel("time")
plt.ylabel("signal")
plt.legend()
plt.show()

w, mag, phase = sig.bode(sys, n=1000)
plt.semilogx(w, mag, label="Magnitude bodeplot")
plt.xlabel("Frequencies")
plt.ylabel("Magnitude")
plt.legend()
plt.show()

Cs = np.array([10, 100, 1000, 10000]) * 10e-6

for c in Cs:
    A = np.array(((-r1 / l1, 0, -1 / l1), (0, -r2 / l2, -1. / l1), (1 / c, 1 / c, 0)))
    sys = sig.StateSpace(A, np.reshape(np.array([1 / l1, 0, 0]), (3, 1)), np.array([0, -r2, 0]), 0)
