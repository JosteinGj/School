import numpy as np
import matplotlib.pyplot as plt
a91samples=np.arange(30)
a91a=np.array( [np.sin(np.sin(4*np.pi*n/20)) for n in a91samples])
a91b= np.array([np.sin(6*np.pi*i/75) for i in a91samples])
def a91c(n):
    return np.exp(2j*np.pi*n/20)
a91cArray = a91c(a91samples)


plt.step(a91samples,a91a)
plt.xlabel("Samples[n]")
plt.ylabel("Signal")
plt.title("Discrete System in A9.1-a)")
plt.savefig("system in 9.1-a.pdf")
plt.show()


plt.step(a91samples,a91b)
plt.xlabel("Samples[n]")
plt.ylabel("Signal")
plt.title("Discrete System in A9.1-b)")
plt.savefig("system in 9.1-b.pdf")
plt.show()


plt.step(a91samples, np.real(a91cArray),label="real part of response")
plt.step(a91samples,  np.imag(a91cArray),label="imaginary part of response")
plt.xlabel("Samples[n]")
plt.ylabel("Signal")
plt.title("Discrete System in A9.1-c)")
plt.savefig("system in 9.1-c.pdf")
plt.show()



plt.step(a91samples,a91a + a91b + np.real(a91cArray),label="real part of response")
plt.step(a91samples,  np.imag(a91cArray),label="imaginary part of response")
plt.xlabel("Samples[n]")
plt.ylabel("Signal")
plt.title("Discrete System in A9.1-d)")
plt.savefig("system in 9.1-d.pdf")
plt.show()









samples = range(30)
time = np.linspace(0, 3, 10000)
a92a = [0.3 ** n for n in samples]
a92b = [0.3 ** n * np.cos(np.pi * n) for n in samples]
a92c = [0.8 ** n  for n in samples]
a92d = [0.8 ** n * np.cos(np.pi * n) for n in samples]
a92aCont = [0.3 ** (10 * t) for t in time]
a92bCont = [0.3 ** (10 * t) * np.cos(np.pi * 10 * t) for t in time]
a92cCont = [0.8 ** (10 * t) for t in time]
a92dCont = [0.8 ** (10 * t) * np.cos(np.pi * 10 * t) for t in time]

tau1 = -1 / (10 * np.log(0.3))
tau2 = -1 / (10 * np.log(0.8))


plt.step(samples, a92a)
plt.xlabel("Samples[n]")
plt.ylabel("Signal")
plt.title("Discrete System in A9.2-a)")
plt.show()

plt.step(samples, a92b)
plt.xlabel("Samples[n]")
plt.ylabel("Signal")
plt.title("Discrete System in A9.2-b)")
plt.show()

plt.step(samples, a92c)
plt.xlabel("Samples[n]")
plt.ylabel("Signal")
plt.title("Discrete System in A9.2-c)")
plt.savefig("a92-c.pdf")
plt.show()

plt.step(samples, a92d)
plt.xlabel("Samples[n]")
plt.ylabel("Signal")
plt.title("Discrete System in A9.2-d)")
plt.savefig("a92-d.pdf")
plt.show()


plt.axvline(tau1,color="darkgrey", linestyle="--",label="tau")
plt.plot(tau1,1/np.e,"rx",label="1/e")
plt.plot(time, a92aCont,label="signal")
plt.legend()
plt.xlabel("Time[s]")
plt.ylabel("Signal")
plt.title("Continous system in A9.2-a)")

plt.show()


plt.plot(time, a92aCont,color="lightgrey",linestyle="-")
plt.axvline(tau1,color="darkgrey", linestyle="--",label="tau")
plt.plot(tau1,1/np.e,"rx",label="1/e")
plt.plot(time,a92bCont,label="signal")
plt.legend()
plt.xlabel("Time[s]")
plt.ylabel("Signal")
plt.title("Continous system in A9.2-b)")
plt.show()

plt.axvline(tau2,color="darkgrey", linestyle="--",label="tau")
plt.plot(tau2,1/np.e,"rx",label="1/e")
plt.plot(time,a92cCont, label="signal")

plt.legend()
plt.xlabel("Time[s]")
plt.ylabel("Signal")
plt.title("Continous system in A9.2-c)")
plt.savefig("cont92-c.pdf")
plt.show()


plt.plot(time, a92cCont,color="lightgrey",linestyle="-")

plt.axvline(tau2,color="darkgrey", linestyle="--",label="tau")
plt.plot(tau2,1/np.e,"rx",label="1/e")
plt.plot(time,a92dCont, label="signal")
plt.legend()
plt.xlabel("Time[s]")
plt.ylabel("Signal")
plt.title("Continous system in A9.2-d)")
plt.savefig("cont92-d.pdf")
plt.show()

# print A9.3 e)
a = 0.5
h = [0, 1 / 4, 1 / 4, 1 / 4, 0, 0, 0, 0, 0, 0]
x = [a ** n for n in range(10)]
print(np.convolve(h, x))
plt.step(range(10),h, label="Transferfunction")
plt.step(range(10),x, label="input signal")
plt.step(range(len(np.convolve(h, x))),np.convolve(h, x), label="output signal")
plt.title(f"system in  A9.3e for a={a}")
plt.xlabel("samples [n]")
plt.ylabel("signal")
plt.legend()
plt.savefig(f"a93-a={a}.pdf")

plt.show()
a = 0.9
x = [a ** n for n in range(10)]
print(np.convolve(h, x))

plt.step(range(10),h, label="Transferfunction")
plt.step(range(10),x, label="input signal")
plt.step(range(len(np.convolve(h, x))),np.convolve(h, x), label="output signal")
plt.title(f"system in  A9.3e for a={a}")
plt.legend()
plt.xlabel("samples [n]")
plt.ylabel("signal")

plt.savefig(f"a93-a={a}.pdf")
plt.show()

