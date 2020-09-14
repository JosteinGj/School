import numpy as np
import scipy.signal as sig
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
plt.title("Impulse response for system in task 6.3 a")
plt.xlabel("time")
plt.ylabel("signal")
plt.legend()
plt.savefig("orgi impresponse sys1.pdf")
plt.show()

stepTime, stepResponse = sig.step(sys, N=10000)
plt.plot(stepTime, stepResponse, label="Step response")
plt.title("step response for system in task 6.3 a")
plt.xlabel("time")
plt.ylabel("signal")
plt.legend()
plt.savefig("orgi step response sys1.pdf")
plt.show()

w, mag, phase = sig.bode(sys, n=1000)
plt.semilogx(w, mag, label="Magnitude bodeplot")
plt.title("Magnitude bodeplot of system in task 6.3 c")
plt.xlabel("Frequencies")
plt.ylabel("Magnitude")
plt.legend()
plt.savefig("mag bode sys1.pdf")
plt.show()


plt.semilogx(w, phase, label="Phase bodeplot")
plt.title("Phase bodeplot of system in task 6.3 a")
plt.xlabel("Frequencies")
plt.ylabel("Phase")
plt.legend()
plt.savefig("phasebode sys1.pdf")
plt.show()

cs = np.array([10, 100, 1000, 10000])*1e-6


for c in cs:
    A = np.array(((-r1 / l1, 0, -1 / l1), (0, -r2 / l2, -1. / l1), (1 / c, 1 / c, 0)))
    sys = sig.StateSpace(A, np.reshape(np.array([1 / l1, 0, 0]), (3, 1)), np.array([0, -r2, 0]), 0)

    impTime, impulseResponse = sig.impulse(sys, T=np.linspace(0,0.1,1000))
    plt.plot(impTime, impulseResponse, label=f"Impulse response c={c}")
    plt.xlabel("time")
    plt.ylabel("signal")
    plt.legend()
plt.savefig("varying c impresponses.pdf")
plt.show()

for c in cs:
    A = np.array(((-r1 / l1, 0, -1 / l1), (0, -r2 / l2, -1. / l1), (1 / c, 1 / c, 0)))
    sys = sig.StateSpace(A, np.reshape(np.array([1 / l1, 0, 0]), (3, 1)), np.array([0, -r2, 0]), 0)

    stepTime, stepResponse = sig.step(sys, T=np.linspace(0,0.1,1000))
    plt.plot(stepTime, stepResponse, label=f"Step response c={c}")
    plt.xlabel("time")
    plt.ylabel("signal")
    plt.legend()
plt.savefig("varying C stepresponses.pdf")
plt.show()

r1 = 100
r2 = 100
l1 = 2
l2 = 5
c = 0.01
A = np.array(((-r1 / l1, 0, -1 / l1), (0, -r2 / l2, -1. / l1), (1 / c, 1 / c, 0)))
numerator = 1000 
denominator = (1, 70, 1070, 2000)
systf = sig.TransferFunction(numerator, denominator)
sys = sig.StateSpace(A, np.reshape(np.array([1/l1, 0, 0]), (3, 1)), np.array([0, -r2, 0]), 0)
wss ,magss, phasess = sig.bode(sys)
wtf, magtf, phasetf = sig.bode(systf)


plt.semilogx(wss, magss, label="Magnitude bodeplot")
plt.xlabel("Frequencies")
plt.ylabel("Magnitude")
plt.legend()
plt.title("Bodeplot of statespace system: magnitude")
plt.savefig("mag bode state sys2.pdf")
plt.show()


plt.semilogx(wss, phasess, label="Phase bodeplot")
plt.xlabel("Frequencies")
plt.ylabel("Phase")
plt.legend()
plt.title("Bodeplot of statespace system: phase")
plt.savefig("phasebode state sys2.pdf")
plt.show()

plt.semilogx(wtf, magtf, label="Magnitude bodeplot")
plt.xlabel("Frequencies")
plt.ylabel("Magnitude")
plt.legend()
plt.title("Bodeplot of transfer function system: magnitude")
plt.savefig("magbode tf sys2.pdf")
plt.show()


plt.semilogx(wtf, phasetf, label="Phase bodeplot")
plt.xlabel("Frequencies")
plt.ylabel("Phase")
plt.legend()
plt.title("Bodeplot of transfer function system: phase")
plt.savefig("phasebode tf sys2.pdf")
plt.show()

