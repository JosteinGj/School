import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import scipy.io.wavfile as wav
import scipy.signal as sig



def bode(filename):
    bodedata = pd.read_csv(filename)
    print(len(bodedata['Frequency (Hz)']))
    plt.semilogx(
        bodedata['Frequency (Hz)'],
        bodedata['Channel 2 Magnitude (dB)'],label="Magnitude response")
    
  
   # plt.vlines(
    #    x=[1.2375e3,1.65e3],
     #   ymin=-10,
      #  ymax=-3,
       # colors="red",label="system criterions"
    #)
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Magnitude (dB)')
    plt.title("Magnitude Bode plot")
    #plt.ylim(-15,1)
    #plt.xlim(5e2,5e3)
    plt.legend(loc="best")
    plt.savefig("eksamen_bode_plot.pdf")
    plt.show()

    plt.semilogx(bodedata['Frequency (Hz)'], bodedata["Channel 2 Phase (deg)"])
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Phaseshift relative input value (deg)')
    plt.title("Phase Bode plot")
    plt.savefig("phase_bodeplot_esda2_designprosjekt6.pdf")
    plt.show()

#bode("eksamen/eksamens_bode_data.csv")



def scope(filename):
    
    scopedata= pd.read_csv(filename)
    
    time, channel_1, channel_2=scopedata["Time (s)"],scopedata["Channel 1 (V)"], scopedata["Channel 2 (V)"]
    
    plt.plot(time,channel_1,label="channel 1")
   # plt.plot(time, channel_2,label="channel_2")
    plt.title("Osciloscope Data")
    plt.legend()
    plt.xlabel("Time (s)")
    plt.ylabel("Signal (V)")
    plt.savefig("ESDA2_design_prosjekt7_scope.pdf")
    plt.show()
    
def spectrum(filename):
    scopedata= pd.read_csv(filename)
    print(scopedata.columns)
    time, channel_1 = scopedata["Frequency (Hz)"],scopedata["Trace 1 (V)"]
    
    plt.plot(time,channel_1,label="channel 1")
    #plt.plot(time, channel_2,label="channel_2")
    plt.title("Spectrum of oscillator sinal")
    plt.legend()
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Signal (V)")
    plt.savefig("ESDA2_design_prosjekt7_spectrum.pdf")
    plt.show()
    
def logic(filename):
    logic_data=pd.read_csv(filename)
    start=0
    stop=950

    time, io_6, io_7=logic_data["Time (s)"], logic_data["DIO 6"], logic_data["DIO 7"]
    print(len(time))
    signalstart=time[io_6==1].values[0]
    print(signalstart)
    periodpoints=[signalstart,signalstart+3.55]
    plt.plot(periodpoints,[0,0],"rx",label="periodmarks")
    plt.plot(time[:stop],io_6[:stop],"C1--",label="IO 6(input indicator)")
    plt.plot(time[:stop],io_7[:stop],label="IO 7(output)")
    plt.xlabel("Time (s)")
    plt.ylabel("Signal")
    plt.title("demodulator output")
    plt.legend(loc="best")
    plt.savefig("D8_demodulator_output.pdf")
    plt.show()



#logic("designprosjekt8/logicOutput_D8.csv")


def scope_to_spectrogram(filename):
    scopedata= pd.read_csv(filename)
    
    time, channel_1, channel_2=scopedata["Time (s)"],scopedata["Channel 1 (V)"], scopedata["Channel 2 (V)"]
    


    f_c2, t_c2, Sxx_c2 = sig.spectrogram(channel_2,10e3)
    plt.pcolormesh(t_c2,f_c2,Sxx_c2,shading="gouraud")
    plt.xlabel("Time [sec]")
    plt.ylabel("Frequencies [Hz]")
    plt.title("Filtered spectogram")
    plt.colorbar()
    plt.savefig("esda_eksamen_filtered spectrogram.pdf")
    plt.show()

    f_c1,t_c1,Sxx_c1=sig.spectrogram(channel_1,10e3)
    plt.pcolormesh(t_c1,f_c1,Sxx_c1,shading="gouraud")
    plt.xlabel("Time [sec]")
    plt.ylabel("Frequencies [Hz]")
    plt.title("Unfiltered spectogram")
    plt.colorbar()
    plt.savefig("esda_eksamen_unfiltered_spectrogram.pdf")
    plt.show()

#scope_to_spectrogram("scope_data_eksamensdata_recorded2.csv")



def spectrum(filename):
    rate,data=wav.read("vedlegg 1.wav")
    rate2,data2=wav.read("vedlegg 2.wav")
    fft2=np.fft.rfft(data2)
    freqs2=np.fft.rfftfreq(len(data2),1/rate2)
    fftdata=np.fft.rfft(data)
    freqs=np.fft.rfftfreq(len(data),1/rate)
    plt.plot(freqs2,abs(fft2/np.max(fft2)), label="Morse signal")
    plt.plot(freqs,abs(fftdata/np.max(fftdata)), label="noisy signal")
    plt.xlabel("frequencies [Hz]")
    plt.ylabel("relative magnitude [1]")
    plt.title("Periodogram of signals")
    plt.legend()
    plt.savefig("esda_eksamen_init_sp.pdf")
    
    plt.show()

#spectrum("vedlegg 1.wav")


def testbp():
    h0=10
    Q=6
    f=600

    num=[h0*2*np.pi*f/Q,0]
    denom=(1,2*np.pi*f/Q,f**2)
    num2=np.convolve(num,num)
    denom2=np.convolve(denom,denom)

    sys = sig.lti(num,denom)
    w,h,p=sig.bode(sys)
    plt.plot(w,h)
    plt.show()
    sys2=sig.lti(num2,denom2)
    w2,h2,p2=sig.bode(sys2)
    plt.plot(w2,h2)
    plt.show()


testbp()