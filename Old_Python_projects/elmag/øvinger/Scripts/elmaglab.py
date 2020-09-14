import numpy as np
import scipy.constants as const
import matplotlib.pyplot as plt
B=np.linspace(0,15,100)
lol=[0.04]*100
U_A_1=20
U_A_2=40
U_A_3=60
r_1=1/B*10**4*np.sqrt(2*U_A_1/(const.e/const.m_e))
r_2=1/B*10**4*np.sqrt(2*U_A_2/(const.e/const.m_e))
r_3=1/B*10**4*np.sqrt(2*U_A_3/(const.e/const.m_e))

plt.plot(B,r_1,label="U=20V")
plt.plot(B,r_2,label="U=40V")
plt.plot(B,r_3,label="U=60V")
plt.plot(B,lol)
plt.ylim(0,0.05)
plt.legend()
plt.show()