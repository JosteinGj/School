import numpy as np
import scipy.signal as signal

import matplotlib.pyplot as plt
import sys
def load_file(filepath):
    return np.loadtxt(filepath)
if len(sys.argv)<3:
    data=load_file("optics_lab/reflect5.txt")
else:
    data=load_file(sys.argv[1])

data = signal.detrend(data, axis=0)
print(data.shape)
r,g,b=data.T
t=np.linspace(0,len(r)*1/40,len(r))

plt.plot(t,r,color="red")
plt.plot(t,g,color="green")
plt.plot(t,b,color="blue")
plt.show()




testing_filter=False
sos = signal.butter(20, [0.6,250/60], "bandpass", False ,"sos",fs=40)

w, h=signal.sosfreqz(sos, worN=np.linspace(0.001,1e1,10000),fs=40)
plt.semilogx(w,np.abs(h))
plt.show()
plt.plot(t,r,color="red")
plt.plot(t,signal.sosfilt(sos,data,axis=0))
plt.show()


data=signal.sosfilt(sos,data,axis=0)
data_fft=np.fft.rfft(data,axis=0)
freq_bins=np.fft.rfftfreq(len(t),1/40)

plt.plot(freq_bins*60,data_fft)
plt.title("lin spectrum")
plt.xlabel("Pulse frequency [bpm]")
plt.ylabel("power density amplitude [Watt]")
plt.xlim(0,250)
plt.show()


plt.plot(freq_bins*60,20*np.log10(np.abs(data_fft)))
plt.title("log spectrum")
plt.xlabel("Pulse frequency [bpm]")
plt.ylabel("power density [watt]")
plt.xlim(0,250)
plt.show()

db_spec = 20 * np.log10(np.abs(data_fft))
maxindicies = np.argmax(db_spec,axis=0)
maxfreqs = [60*freq_bins[i] for i in maxindicies]
print("maxfreqs: ", maxfreqs)
print(np.average(db_spec[20:30,:],axis=0))
noisefloor=(np.average(db_spec[20:30,:]) + np.average(db_spec[40:250,:]))/2
print(np.max(db_spec),noisefloor,np.max(db_spec)-noisefloor)