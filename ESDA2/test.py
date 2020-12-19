import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sig
import scipy.io.wavfile as waveyboi


def FSK(file):
    def mean_filter(N):
        return 1/N*np.ones(N)


    fs,y=waveyboi.read(file)
    print(len(y)/fs)
    quit()
    fft_y=np.fft.rfft(y)
    fft_bins=np.fft.rfftfreq(len(y),1/fs)
    plt.plot(fft_bins[:len(fft_bins)//20], np.abs(fft_y[:len(fft_bins)//20])/np.max(np.abs(fft_y[:len(fft_bins)//20])))
    plt.xlabel("Freqency")
    plt.ylabel("Relative amplitude")
    plt.title("relative spectral density of signal")
    plt.savefig(f"ESDA_D8_spectral_density.pdf")
    plt.show()
    sos_low = sig.butter(1, 500, 'low', analog=False, fs=fs, output="sos")
    sos_high = sig.butter( 1, 500, 'high', analog=False, fs=fs, output="sos")
    b_low,a_low = sig.butter(1, 500, 'low', analog=False, fs=fs, output="ba")  
    bhigh,ahigh = sig.butter( 1, 500, 'high', analog=False, fs=fs, output="ba")
    print(b_low,a_low)
    print(bhigh,ahigh)
    low_filtered =  sig.sosfilt(sos_low, y)
    low_filtered=np.convolve(np.abs(low_filtered),mean_filter(100))
    plt.plot(low_filtered)
    plt.title("low filtered filtered")
    plt.show()



    high_filtered = sig.sosfilt(sos_high, y)
    high_filtered=np.convolve(np.abs(high_filtered),mean_filter(100))
    plt.plot(high_filtered)
    plt.title("high filtered filtered")
    plt.show()

    plt.plot(low_filtered)
    plt.plot(high_filtered)
    plt.show()
    
    digitalized=[f1>f0 for f1,f0 in zip(np.abs(high_filtered),np.abs(low_filtered))]
    
    lowsig=sig.sosfilt(sos_high, y)
    
    plt.plot(np.linspace(0,len(lowsig)/fs,len(lowsig)),lowsig/np.max(lowsig))
    plt.plot(np.linspace(0,len(lowsig)/fs,len(digitalized)),digitalized)
    plt.title("digitalized")
    plt.xlabel("Time (s)")
    plt.title("signal with output overlayed")
    plt.savefig("signal with overlayed output.")
    plt.show()

FSK("FSK26.wav")