import scipy.signal as sig
import scipy.stats as stats
import scipy.io.wavfile as wav
import numpy as np
import numpy.linalg as la
import matplotlib.pyplot as plt

import sounddevice as sd


from pysptk import lpc




def task2():
    wgn = stats.norm.rvs(size=int(1e6))
    x = sig.lfilter([1,-1/2],1,wgn)
    
    y0 = 5 / 4
    y1 = -1 / 2
    def calc_perdictor_coefs(p=False):
        order3 = [y1, 0, 0]
        order2 = [y1, 0]
        order1 = [y1]
        AlLSyStEmSwIlLBoWToThE3RdOrder = np.matrix([
            [y0, y1, 0],
            [y1, y0, y1],
            [0, y1, y0]])
        AlLSyStEmSwIlLBoWToThE2NdOrder = np.matrix([
            [y0, y1],
            [y1, y0]])
        AlLSyStEmSwIlLBoWToThE1StOrder = np.matrix([[y0]])

        sol3 = la.solve(AlLSyStEmSwIlLBoWToThE3RdOrder, order3)
        
        sol2 = la.solve(AlLSyStEmSwIlLBoWToThE2NdOrder, order2)
        
        sol1 = la.solve(AlLSyStEmSwIlLBoWToThE1StOrder, order1)
        if p:
            print(sol1)
            print(sol2)
            print(sol3)
        return sol1, sol2, sol3
    i=1
    filters = calc_perdictor_coefs(True)
    for filth in filters:
        f = filth
        filth = np.insert(arr=filth, obj=0, values=1)
        
        
        x_pred = sig.lfilter(filth, 1, x)
        mse=((x - x_pred) ** 2).mean(axis=0)
        print("mse: ",mse)
        print("filth: ",filth)
        w, h = sig.freqz(filth,mse,worN=2048)
        
        plt.plot(w,h*np.conj(h),label="freqz output")
        if i==1:
            plt.plot(w,1.4-0.8*np.cos(w),label="calculated PDS estimate")
        elif i==2:
            plt.plot(w,g(1+f[0]**2+f[1]**2) + 2*(f[0] + f[1]*f[0])*np.cos(w) + 2* f[1] *np.cos(2*w),label="calculated PDS estimate")
        elif i==3:
            plt.plot(w,(1 + f[0]**2 + f[1]**2 + f[2]**2) + 2*(f[0] + f[1]*f[0] + f[2]*f[1])*np.cos(w) + 2*(f[1] + f[0]*f[2])*np.cos(2*w) + 2*f[2]*np.cos(3*w),label="calculated PDS estimate")

        plt.plot(w,5/4-np.cos(w),label="analytic PDS")
        plt.legend()
        plt.title(f"Estimated PDS for AR({i}) estimate ")
        plt.xlabel("Frequency (rad s^-1)")
        plt.ylabel("Amplitude response")
        plt.savefig(f"Task2_{i}order_PDS_estimate.pdf")
        i+=1
        plt.show()


task2()

def task3():

    def lpc(data,order=10):
        data=data.astype("int64")
        acf=sig.correlate(in1=data, in2=data, mode="full",method="direct")
        mid=len(acf)//2
        matrix=np.array([acf[mid-i:mid-i+order] for i in range(order)])
        print(matrix.dtype)
        gammavec=acf[mid+1:mid+1+order]
        sol=la.solve(matrix,gammavec)
        print(sol)
        return sol
    rate,data_a=wav.read(f"oving8/vowels/a.wav")
    _, data_ae=wav.read("oving8/vowels/ae.wav")
    a = lpc(data_a)
    b = lpc(data_ae)
    filtered_a=sig.lfilter(b, a, data_ae)
    wav.write("filtered_a.wav",rate,filtered_a)
    

#task3()  

