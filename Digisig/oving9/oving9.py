import numpy as np
import scipy.signal as sig
import matplotlib.pyplot as plt
import scipy.signal.windows as win

def task1():
    def approx_lowpass_filter(fc,window):
        N=len(window)
        n=np.arange(0,N)
        n[(N-1)//2]=0

        h=(np.sin(2*np.pi*fc*(n-(N-1)//2)) / (np.pi*(n-(N-1)//2)))*window

        h[(N-1)//2]=2*fc*window[(N-1)//2]
        return h

    plt.stem(approx_lowpass_filter(0.2,np.ones(31)))
    plt.show()
    window1=np.ones(31)
    window2=np.hamming(31)
    w1,h1=sig.freqz(approx_lowpass_filter(0.2,window1),worN=1000)
    w2,h2=sig.freqz(approx_lowpass_filter(0.2,window2),worN=1000)

    plt.plot(w1,np.abs(h1))
    plt.xlabel("frequecies (radians/sample)")
    plt.ylabel("magnitude")
    plt.title("magnitude response of 'manual' filter with rectangular window")
    plt.savefig("digsig9_task1_man_rekt_lowpass_mag_response.pdf")
    plt.show()
    
    plt.xlabel("frequecies (radians/sample)")
    plt.ylabel("magnitude")
    plt.title("magnitude response of 'manual' filter with hamming window")
    plt.savefig("digsig9_task1_man_ham_lowpass_mag_response.pdf")
    plt.plot(w2,np.abs(h2))
    plt.show()


    h3 = sig.firwin(31,0.2,window="boxcar",pass_zero="lowpass",fs=1)
    h4 = sig.firwin(31,0.2,window="hamming",pass_zero="lowpass",fs=1)
    
    w3,h3=sig.freqz(h3,worN=1000)
    w4,h4=sig.freqz(h4,worN=1000)

    plt.plot(w3,np.abs(h3))
    plt.xlabel("frequecies (radians/sample)")
    plt.ylabel("magnitude")
    plt.title("magnitude response of 'auto' filter with rectangular window")
    plt.savefig("digsig9_task1_auto_rekt_lowpass_mag_response.pdf")
    plt.show()
    plt.plot(w4,np.abs(h4))
    plt.xlabel("frequecies (radians/sample)")
    plt.ylabel("magnitude")
    plt.title("magnitude response of 'auto' filter with hamming window")
    plt.savefig("digsig9_task1_auto_ham_lowpass_mag_response.pdf")
    plt.show()

task1()


def task2():

    b=0.245*np.ones(2)
    a=np.array([1, -0.51])

    w, h=sig.freqz(b,a,worN=1000,fs=1)
    plt.plot(w,h)
    plt.xlabel("normalized frequency ")
    plt.ylabel("magnitude")
    plt.title("magnitude repsonse of digitalized filter")
    plt.savefig("digsig9_task2_digitalized_mag_resp.pdf")
    plt.show()

#task2()
def task3():
    b,a = sig.butter(2,1,analog=True)
    w,h = sig.freqs(b, a, worN=1000)
    plt.plot(w, 20*np.log10(np.abs(h)/max(np.abs(h))))
    plt.xlabel("frequency")
    plt.ylabel("magnitude")
    plt.title("magnitude response of analog filter")
    plt.savefig("digsig9_task3_analog_filter_mag_resp.pdf")
    plt.show()

    T1=0.25
    T2=1.2
    def linsys(T):
        num=[0, np.sqrt(2) * np.exp(-T / np.sqrt(2)) * np.sin(T / np.sqrt(2))]
        denom = [1,-2 * np.exp(-T / np.sqrt(2)) * np.cos(T / np.sqrt(2)), np.exp(-np.sqrt(2)*T)]
        return num, denom
    
    num1,denom1=linsys(T1)
    num2,denom2=linsys(T2)

    w1,h1=sig.freqz(num1,denom1)
    
    w2,h2=sig.freqz(num2,denom2)
    plt.plot(w1,20*np.log10(np.abs(h1)/max(np.abs(h1))))
    plt.xlabel("normalized frequency")
    plt.ylabel("magnitude( db)")
    plt.title(f"magnitude response of digital filter with w_c={T1}")
    plt.savefig(f"digsig9_task3d_digitalfilter_wc={T1}.pdf")
    plt.show()
    plt.plot(w2,20*np.log10(np.abs(h2)/max(np.abs(h2))))
    plt.xlabel("normalized frequency")
    plt.ylabel("magnitude( db)")
    plt.title(f"magnitude response of digital filter with w_c={T2}")
    plt.savefig(f"digsig9_task3d_digitalfilter_wc={T2}.pdf")
    plt.show()


#task3()