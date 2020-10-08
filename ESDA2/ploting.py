import matplotlib.pyplot as plt
import numpy as np
import pandas as pd




def bode():
    bodedata = pd.read_csv("bodedata.csv")
    plt.semilogx(bodedata['Frequency (Hz)'], bodedata['Channel 2 Magnitude (dB)'])
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Dropoff from input value (dB)')
    plt.ylim(-1,0)
    plt.title("Magnitude Bode plot for buffer")
    plt.savefig("magbodeplot_esda2_designprosjekt.pdf")
    plt.show()
    print(bodedata.columns)

    plt.semilogx(bodedata['Frequency (Hz)'], bodedata["Channel 2 Phase (deg)"])
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Phaseshfit relative input value (deg)')

    plt.title("Phase Bode plot for buffer")
    plt.savefig("phase_bodeplot_esda2_designprosjekt.pdf")
    plt.show()

def scope():
    
    scopedata= pd.read_csv("scopedata.csv")
    
    time,channel_1,channel_2=scopedata["Time (s)"],scopedata["Channel 1 (V)"], scopedata["Channel 2 (V)"]
    
    plt.plot(time,channel_1,label="channel 1")
    plt.plot(time, channel_2,label="channel_2")
    plt.title("osciloscope values at 1kHz, A_0 = 0.5V")
    plt.legend()
    plt.xlabel("Time (s)")
    plt.ylabel("Signal (V)")
    plt.savefig("scope_1kHz_amp=0.5V.pdf")
    plt.show()
    
    absdiff=(channel_1-channel_2)
    plt.plot(time,absdiff)
    plt.title("Difference in signals at 1kHz, A_0 = 0.5V")
    plt.ylabel("Difference (V)")
    plt.xlabel("Time (s)")
    plt.savefig("diff_1khz_amp=0.5V.pdf")
    plt.show()

    # 1.4V data
    scopedata=pd.read_csv("scopedata1.4V.csv")
    time,channel_1,channel_2=scopedata["Time (s)"],scopedata["Channel 1 (V)"], scopedata["Channel 2 (V)"]
    
    plt.plot(time,channel_1,label="channel 1")
    plt.plot(time, channel_2,label="channel_2")
    plt.title("osciloscope values at 1kHz, A_0 = 1.4V")
    plt.legend()
    plt.xlabel("Time (s)")
    plt.ylabel("Signal (V)")
    plt.savefig("scope_1kHz_amp=1.4V.pdf")
    plt.show()
    
    absdiff=(channel_1-channel_2)
    plt.plot(time,absdiff)
    plt.title("Difference in signals at 1kHz, A_0 = 1.4V")
    plt.ylabel("Difference (V)")
    plt.xlabel("Time (s)")
    plt.savefig("diff_1khz_amp=1.4V.pdf")

    plt.show()

scope()
