import numpy as np
import scipy.signal as sig
import matplotlib.pyplot as plt


R=1000
L=1e-1
C=1e-6
print(L,C)
num, denom = 1, sig.convolve([1,-1000],[1,-1000])
print(denom)
num2,denom2 = [1,0], [R*C,1,R/L]

sys=sig.TransferFunction(num,denom)
sys2=sig.TransferFunction(num2,denom2)


w, mag, ph = sig.bode(sys,n=10000000)
w2,mag2,ph2 =sig.bode(sys2,n=10000000)


plt.semilogx(w,mag)
plt.xlabel("freqency (w)")
plt.ylabel("magnituede")
plt.savefig("mag_resp_edsa2_4.1c.pdf")
plt.show()
plt.semilogx(w,ph)
plt.xlabel("freqency (w)")
plt.ylabel("phase")
plt.savefig("ph_resp_edsa2_4.1c.pdf")
plt.show()


plt.semilogx(w2,mag2)
plt.xlabel("freqency (w)")
plt.ylabel("magnituede")
plt.savefig("mag_resp_edsa2_4.1c_para.pdf")
plt.show()