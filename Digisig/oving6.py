import scipy.signal as sig
import numpy as np
import numpy.fft as fft
import matplotlib.pyplot as plt


def task1():
    N_x=28
    def system(N_x=28, a=0.9):
        numerator = np.zeros(N_x + 1)
        denom = np.zeros(2)
        numerator[0], numerator[N_x] = 1, -a ** N_x
        denom[0], denom[1] = 1, -a
        return numerator, denom
    num, denom = system()

    w_whole, h_whole = sig.freqz(num, denom, whole=True, worN=2048)
    w, h = sig.freqz(num, denom, worN=2048)
    plt.plot(w_whole/ (2 * np.pi), h_whole)
    plt.xlabel("normalized freq (cycles/sample)")
    plt.ylabel("magnitude")
    plt.title("Magnitude spectrum")
    plt.savefig("digsig6_task1_magnitude_of_spectrum_in_1a.pdf")
    plt.show()
    plt.Figure()
    x = [0.9 ** n for n in range(N_x)]
    fft_lengths = [N_x // 4, N_x // 2, N_x, 2 * N_x]
    ffts=[(fft.rfft(x, length),fft.rfftfreq(length)) for length in fft_lengths]
    print(fft.rfftfreq(N_x//4))
    print(fft.rfftfreq(N_x//2))
    print(fft.rfftfreq(N_x))
    print(fft.rfftfreq(2*N_x))
    i=0
    for spec,freq in ffts:
        
        plt.plot(w/(2*np.pi),h,color="C0")
        plt.stem(freq,spec)
        
        plt.xlabel("normalized freq up to half nyquist freqency")
        plt.ylabel("magnitude")
        plt.title(f"DFT of signal with len={fft_lengths[i]}")
        plt.savefig(f"digsig6_task1_magnitude_DFT_in_1a_len={fft_lengths[i]}.pdf")
        plt.show()
        i+=1
    
    
task1()


def task2():
    N_x=36
    x=np.array([0.9**n for n in range(28)])
    h=np.ones(9)

    y=np.convolve(x,h)
    plt.stem(y)
    plt.xlabel("samples")
    plt.ylabel("magnitude")
    plt.title(f"TimeDomain analysis of signal")
    plt.savefig(f"digsig6_task2_TimeDomainAnalysis_len={36}.pdf")    
    plt.show()
    print(len(y))

    X=fft.rfft(x,n=36)
    H=fft.rfft(h,n=36)
    Y = X*H
    y2= fft.irfft(Y,n=36)
    plt.stem(y2)
    plt.xlabel("samples")
    plt.ylabel("magnitude")
    plt.title(f"DFT analysis of signal")
    plt.savefig(f"digsig6_task2_DFTAnalysis_len={36}.pdf")    
    plt.show()

    fft_lengths = [N_x // 4, N_x // 2, N_x, 2 * N_x]
    def fftconv(sig, length, transfer=h):
        X=fft.rfft(sig,n=length)
        H=fft.rfft(transfer,n=length)
        Y = X*H
        return fft.irfft(Y,n=length)
    
    for length in fft_lengths:
        #plt.stem(y,linefmt="C0-",markerfmt="C0o",label="time domain convolved signal")
        plt.stem(fftconv(x, length),linefmt="C1-",markerfmt="C1o",label=f"y at n={length}")
        
        plt.xlabel("samples")
        plt.ylabel("magnitude")
        plt.title(f"DFT analysis compared to time domain convolution")
        plt.legend(loc="upper right")
        plt.savefig(f"digsig6_task2_DFTtoTimeDomainAnalysis_len={length}.pdf")
        plt.show()
    



task2()

def task3():
    ks=[10,30,100,1000]
    dftlen=[128,256,1024]
    def x(lenght):
        f1 = 7/40
        f2 = 9/40
        n=np.arange(lenght)
        return np.sin(2*np.pi*f1*n)+np.sin(2*np.pi*f2*n)
    for k in ks:
        for length in dftlen:
            plt.plot(fft.rfftfreq(length),np.abs(fft.rfft(x(k),n=length)))
            plt.xlabel("normalized frequency")
            plt.ylabel("magnitude")
            plt.title(f"spectrum of signal with len={k} and {length} frequency bins")
            plt.savefig(f"digsig6_task3_SpectrumOfSignal_Len={k},dftlen{length}.pdf")
            plt.show()
    
#task3()
    