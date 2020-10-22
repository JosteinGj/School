import numpy as np
import scipy.stats as stats
import scipy.signal as sig
import matplotlib.pyplot as plt




def white_binary_noise(length):
    signal= stats.uniform.rvs(size=length)
    signal=[-1 if i<0.5 else 1 for i in signal]
    return np.array(signal)


def task1(a=True,c=True):
    if a:
        length=100
        plt.stem(stats.norm.rvs(size=length))
        plt.xlabel("samples")
        plt.ylabel("value")
        plt.title(f"white gaussian noise signal, length: {length}")
        plt.savefig(f"DigSig7_Task1_whiteGaussNoiseLen={length}.pdf")
        plt.show()    

        plt.stem(white_binary_noise(length))
        plt.ylabel("value")
        plt.xlabel("samples")
        plt.title(f"White binary noise of length {length}")
        plt.savefig(f"DigSig7_Task1_WhiteBinaryNoiseLen={length}")
        plt.show()

        plt.stem(stats.uniform.rvs(scale=2*np.sqrt(3),size=length)-np.sqrt(3))
        plt.xlabel("samples")
        plt.ylabel("value")
        plt.title(f"white uniform noise signal, length: {length}")
        plt.savefig(f"DigSig7_Task1_WhiteUniformNoiseLen={length}.pdf")
        plt.show()
    if c:
        length=20000
        wgn = stats.norm.rvs(size=length)
        wun = stats.uniform.rvs(scale=2*np.sqrt(3),size=length)-np.sqrt(3)
        wbn = white_binary_noise(length)

        wgn_mean = np.mean(wgn)
        wun_mean = np.mean(wun)
        wbn_mean = np.mean(wbn)
        print(wgn_mean,wun_mean,wbn_mean)
        
        acf=sig.correlate(wgn,wgn)
        plt.stem(np.arange(-10,11),acf[len(acf)//2-10:len(acf)//2+11])
        plt.xlabel("Delay")
        plt.ylabel("Correlation")
        plt.title("Auto correlation of WGN signal")
        plt.savefig("DigSig7_Task1b_ACF_WGN.pdf")
        plt.show()

        acf=sig.correlate(wun,wun)
        plt.stem(np.arange(-10,11),acf[len(acf)//2-10:len(acf)//2+11])
        plt.xlabel("Delay")
        plt.ylabel("Correlation")
        plt.title("Auto correlation of WUN signal")
        plt.savefig("DigSig7_Task1b_ACF_WUN.pdf")
        plt.show()

        acf=sig.correlate(wbn,wbn)
        plt.stem(np.arange(-10,11),acf[len(acf)//2-10:len(acf)//2+11])
        plt.xlabel("Delay")
        plt.ylabel("Correlation")
        plt.title("Auto correlation of WBN signal")
        plt.savefig("DigSig7_Task1b_ACF_WBN.pdf")
        plt.show()

# task1()


def task2():
    expected_value = 0
    exact_acf =  np.array([(-1/2)**abs(n) for n in range(-10,11)])
    exact_pds = 3 / (5-4*np.cos(2*np.pi*np.linspace(-0.5,0.5,39999)))
    exact_power = 1
    num, den = [1], [1, 1 / 2]
    wgn = stats.norm.rvs(scale=9/16, size=20000)
    x = sig.lfilter(num, den, wgn)
    plt.plot(x)
    plt.show()
    plt.plot(wgn)
    plt.show()

    mean = np.mean(x)
    acf = sig.correlate(x, x)
    pds = np.fft.fft(acf)
    power = acf[len(acf)//2]/8450
    print("power: ", power)
    print("mean: ", mean)

    plt.stem(range(-10,11),acf[len(acf)//2-10:len(acf)//2+11],label="aprox")
    plt.xlabel("Delay")
    plt.ylabel("Correlation")
    plt.title("Auto correlation of task 2 signal")
    plt.legend(loc="best")
    plt.savefig("DigSig7_Task2a_ACF_est.pdf")
    plt.show()
    
    plt.stem(range(-10,11),exact_acf)
    plt.xlabel("Delay")
    plt.ylabel("Correlation")
    plt.title("Auto correlation of task 2 signal")
    plt.legend(loc="best")
    plt.savefig("DigSig7_Task2a_ACF_exactamente.pdf")
    plt.show()


    partioned_arrays_k10= np.split(x,10)
    spec10=[]
    for arr in partioned_arrays_k10:
        spec10.append(np.abs(np.fft.fft(arr,norm="ortho"))**2)
    pds10=(np.average(np.array(spec10),axis=0))
    
    plt.stem(np.fft.fftfreq(pds10.shape[0]),pds10,label="PDS estimate")
    plt.xlabel("frequency")
    plt.ylabel("power density")
    plt.legend(loc="best")
    plt.title("power spectrum estimate of task 2 signal with 10 partitions")
    plt.savefig("DigSig7_Task2a_PDS_10bin.pdf")
    plt.show()

    plt.stem(np.fft.fftfreq(len(pds)),np.abs(pds)**2,label="PDS estimate")
    plt.xlabel("frequency")
    plt.ylabel("power density")
    plt.legend(loc="best")
    plt.title("power spectrum estimate of task 2 signal")
    plt.savefig("DigSig7_Task2a_PDS.pdf")
    plt.show()

    plt.plot(np.fft.fftfreq(39999),exact_pds,label="Exact PDS")
    plt.xlabel("Frequency")
    plt.ylabel("Power density")
    plt.legend(loc="best")
    plt.title("Exact power spectrum of task 2 signal")
    plt.savefig("DigSig7_Task2a_PDS_exact.pdf")
    plt.show()


    partioned_arrays_k100= np.split(x,100)
    spec100=[]
    for arr in partioned_arrays_k100:
            spec100.append(np.abs(np.fft.fft(arr,norm="ortho"))**2)
    pds100=(np.average(np.array(spec100),axis=0))
    
    plt.stem(np.fft.fftfreq(pds100.shape[0]),pds100,label="PDS estimate")
    plt.xlabel("frequency")
    plt.ylabel("power density")
    plt.legend(loc="best")
    plt.title("power spectrum estimate of task 2 signal with 100 partitions")
    plt.savefig("DigSig7_Task2a_PDS_100bin.pdf")
    plt.show()


    ###########################################################
    # task 3
    k=[20,40,100]
    for val in k:
        x_part=np.array([x[val*i:val*(i+1)] for i in range(200)])
        averages=np.mean(x_part,axis=1)
        print(averages.shape)
        plt.hist(averages,20)
        plt.xlabel("mean values")
        plt.ylabel("realization count")
        plt.title(f"Histogram of mean estimates for K={val}")
        plt.savefig(f"DigSig7_task3_MeanHist_K={val}.pdf")
        plt.show()
        print(f"mean of means N={val}: ", np.mean(averages.flatten()))
        print(f"variance of estimator N={val}: ",np.var( averages.flatten()))
        



task2()
