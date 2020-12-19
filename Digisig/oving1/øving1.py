import numpy as np
import scipy.signal as sig
import matplotlib.pyplot as plt

def task1b():
    k = 100000
    M = 10
    w = np.linspace(-np.pi, np.pi, k)
    matrix = np.ones((2 * M, k))
    for i in range(1, 2 * M):
        matrix[i, :]=2 * np.cos(M*w)
    func=np.sum(matrix,axis=0)
    plt.plot(w,func)
    plt.show()

#task1b()

def task3c():
    sys1_num = [1, 2, 1]
    sys1_denom = [1]
    sys2_num = [1, 0]
    sys2_denom =[1, 0.9]
    sys1_gain = 1 
    sys1_zeros=[-1, -1]
    sys1_poles=[]
    sys1 = sig.dlti(sys1_num,sys1_denom)
    sys2 = sig.dlti(sys2_num,sys2_denom)
    w1, mag1, phase1 = sig.dbode(sys1, n=100000)
    w2, mag2, phase2 = sig.dbode(sys2, n=100000)
    plt.semilogx(w1, mag1)
    plt.title("magnitude response of first system")
    plt.savefig("task3c mag1.pdf")
    plt.show()
    
    plt.semilogx(w1, phase1)
    plt.title("phase response of first system")
    plt.savefig("task3c phase1.pdf")
    plt.show()

    plt.semilogx(w2, mag2)
    plt.title("magnitude response of second system")
    plt.savefig("task3c mag2.pdf")
    plt.show()
    
    plt.semilogx(w2, phase2)
    plt.title("phase response of second system")
    plt.savefig("task3c phase2.pdf")
    plt.show()
    sys1 = sig.ZerosPolesGain(sys1_zeros,)
    n = np.arange(1000)
    x = 1 / 2 * np.sin(np.pi * n + np.pi / 4)
    out1 = sig.dlsim(sys1, x)
    out2 = sig.dlsim(sys2, x)

    plt.plot(n,out1)
    plt.title("output of system 1")
    plt.savefig("task3e output1.pdf")
    plt.show()
    
    plt.plot(n,out2)
    plt.title("output of system 2")
    plt.savefig("task3e output2.pdf")
    plt.show()

task3c()

def task4():
    x=np.linspace(0, 1)
    x=np.cos(2000 * np.pi*n*T)