import scipy.signal as sig
import matplotlib.pyplot as plt
import numpy as np
from scipy.io import loadmat, wavfile

def task1():
    a_vals = [0.5, 0.9, -0.9]
    ws = np.linspace(-0.5,0.5,10000)
    f = np.linspace(-1/4,1/4,10000)
    l=list(np.arange(-50,51))
    xs=[]
    autocorrs=[]
    specdensity=[]
    energies=[]
    for a in a_vals:
        xs.append([a**n for n in range(50)])
        autocorrs.append([a ** abs(l) / (1+a**2) for l in range(-50,51)])
        specdensity.append([1/(1+a*np.cos(2*np.pi*w)+a**2) for w in ws])

    
    for i in range(3):
        plt.stem(xs[i],label=f"signal for a={a_vals[i]}")
        plt.xlabel("Samples (n)")
        plt.ylabel("Signal value")
        plt.title(f"Signal: a={a_vals[i]}")
        plt.legend(loc="upper right")
        plt.savefig(f"1b_signal_a={a_vals[i]}_digsig_5.pdf")
        plt.show()
        

        plt.stem(l,autocorrs[i],label=f"Autocorrelation for a={a_vals[i]}")
        plt.xlabel("delay (l)")
        plt.ylabel("Signal value")
        plt.title(f"Autocorrelation: a={a_vals[i]}")
        plt.legend(loc="upper right")
        plt.savefig(f"1b_autocorr_a={a_vals[i]}_digsig_5.pdf")
        plt.show()

        plt.plot(ws,specdensity[i],label=f"spectral density for a={a_vals[i]}")
        plt.xlabel("normalized freqency")
        plt.ylabel("Density")
        plt.title(f"Spectral density: a={a_vals[i]}")
        plt.legend(loc="upper right")
        plt.savefig(f"1b_spectral_density_a={a_vals[i]}_digsig_5.pdf")
        plt.show()

        energy=abs(np.array(xs[i]))**2
        print(np.sum(energy))
        energies.append(energy)

    plt.plot(f, np.cos(2 * np.pi * f), label=f"S_yy(f)")
    plt.xlabel("normalized freqency")
    plt.ylabel("Density")
    plt.title(f"Spectral density y [Syy(f)]")
    plt.legend(loc="upper right")
    plt.savefig(f"1e_spectral_density_of_y_digsig_5.pdf")
    plt.show()

    print(sum(abs(np.cos(2*np.pi*f)**2)))
        
# task1
def task2():
    vals = loadmat("signals.mat") 
    print(vals.keys())
    x,y = np.array(vals["x"]).flatten(), np.array(vals["y"]).flatten()
    print("x: ",x,"y: ",y,sep="\n")

    plt.stem(x,label="outgoing signal")
    plt.xlabel("Samples (n)")
    plt.ylabel("Signal value")
    plt.title(f"Signal x")
    plt.legend(loc="upper right")
    plt.savefig(f"signal_2a_x_digsig_5.pdf")
    plt.show()
    
    plt.stem(y,label="incoming signal")
    plt.xlabel("Samples (n)")
    plt.ylabel("Signal value")
    plt.title(f"Signal y")
    plt.legend(loc="upper right")
    plt.savefig(f"signal_2a_y_digsig_5.pdf")
    plt.show()
    print(len(x),len(y),sep="\n")
    r_xy = sig.correlate(x,y)
    r_yx = sig.correlate(y,x)
    plt.stem(np.arange(-len(x),len(x)-1),r_xy,label="Cross correlation_xy")
    plt.xlabel("delay")
    plt.ylabel("coorelation value")
    plt.title("Crosscorrelation plot")
    plt.legend(loc="upper right")
    plt.savefig("crossCorr_xy_2b_digsig_5.pdf")
    plt.show()

    plt.stem(np.arange(-len(x),len(x)-1),np.flip(r_yx),label="flipped Cross correlation r_yx")
    plt.xlabel("delay")
    plt.ylabel("coorelation value")
    plt.title("flipped Crosscorrelation r_yx plot")
    plt.legend(loc="upper right")
    plt.savefig("flipped_CrossCorr_yx_2b_digsig_5.pdf")
    plt.show()


#task2()


def task3():
    def echoFilter(a, R):
        numerator, denominator = np.zeros(R + 1), 1
        numerator[0], numerator[R] = 1, a
        return numerator, denominator
    a_vals, R_vals = [0.7, 0.5], [5, 10] 
    rate, data = wavfile.read("piano.wav")
    wavfile.write(f"piano1.wav",rate,data)
    impulse = np.zeros(100)
    impulse[0] = 1
    for a in a_vals:
        for R in R_vals:
            num, denom = echoFilter(a, R)
            y = sig.lfilter(num, denom, impulse)
            w, h = sig.freqz(num, denom)
            yout=sig.lfilter(num, denom, data)
            wavfile.write(f"piano_a={a}R={R}.wav", rate, yout)

            plt.stem(y,label="impulse response")
            plt.xlabel("samples")
            plt.ylabel("signals amplitude")
            plt.title(f"impulse response a={a}, R={R}")
            plt.legend(loc="upper right")
            plt.savefig(f"task3_echo_filter_impResp_a={a}R={R}.pdf")
            plt.show()

            plt.plot(w,h,label="frequency response")
            plt.xlabel("normalized freqency")
            plt.ylabel("amplitude")
            plt.title(f"freqency response a={a}, R={R}")
            plt.legend(loc="upper right")
            plt.savefig(f"task3_echo_filter_freqResp_a={a}R={R}.pdf")
            plt.show()

            plt.plot(yout)
            plt.xlabel("time (s)")
            plt.ylabel("signal amplitude")
            plt.title(f"Filtered piano a={a}, R={R}")
            plt.legend(loc="upper right")
            plt.savefig(f"task3_Filtered_piano_a={a}R={R}.pdf")
            plt.show()

    

#task3()

def task3_part2():
    def echoFilter2(a, R, N):
        numerator, denominator =np.zeros( R*(N + 1)), np.zeros(R+1) 
        numerator[0], numerator[N * R] =  1, - 1 * (a ** N)
        denominator[0], denominator[R] = 1, -a
        return numerator, denominator
    
    a_vals = [0.5, 0.7]
    R_vals = [5, 10]
    N_vals = [5, 10]
    rate, data = wavfile.read("piano.wav")
    impulse = np.zeros(100)
    impulse[0] = 1
    plt.plot(data)
    plt.xlabel("time (s)")
    plt.ylabel("signal amplitude")
    plt.title(f"Origianl piano signal")
    plt.legend(loc="upper right")
    plt.savefig(f"task3_unFiltered_piano.pdf")
   # plt.show()
    for a in a_vals:
        for R in R_vals:
            for N in N_vals:
                num, denom=echoFilter2(a, R, N)
                y=sig.lfilter(num,denom,impulse)
                
                w, h = sig.freqz(num,denom)

                #print(y)
                
                plt.stem(y,label="impulse response")
                plt.xlabel("samples")
                plt.ylabel("signals amplitude")
                plt.title(f"impulse response a={a}, R={R}, N={N}")
                plt.legend(loc="upper right")
                plt.savefig(f"task3_echo_filter_impResp_a={a}R={R}N={N}.pdf")
                plt.show()

                plt.plot(w,h,label="frequency response")
                plt.xlabel("normalized freqency")
                plt.ylabel("amplitude")
                plt.title(f"freqency response a={a}, R={R}, N={N}")
                plt.legend(loc="upper right")
                plt.savefig(f"task3_echo_filter_freqResp_a={a}R={R}N={N}.pdf")
                plt.show()
                
                yout=sig.lfilter(num,denom,data)
                wavfile.write(f"piano_a={a}R={R}N={N}.wav",rate,yout)
                plt.plot(yout)
                plt.xlabel("time (s)")
                plt.ylabel("signal amplitude")
                plt.title(f"Filtered piano a={a}, R={R}, N={N}")
                plt.legend(loc="upper right")
                plt.savefig(f"task3_Filtered_piano_a={a}R={R}N={N}.pdf")
                plt.show()
    
task3_part2()