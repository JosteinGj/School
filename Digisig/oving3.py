import scipy.signal as sig
import numpy as np
import matplotlib.pyplot as plt


sys= sig.lti([1, 0, -1],[1,0,0.25])

w, mag, ph = sig.bode(sys,n=10000)
plt.semilogx(w,mag)
plt.show()
plt.semilogx(w,ph)
plt.show()
