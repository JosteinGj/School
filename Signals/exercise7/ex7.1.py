import numpy as np
import scipy.signal as sig
import matplotlib.pyplot as plt


def system87():
    A = np.array([[-6, -5], [1, 0]])
    B = np.array([[0], [2]])
    C = np.array([1, 1])
    D = np.array([[2]])
    sys = sig.lti(A, B, C, D)
    t = np.linspace(0, 0.01, 1000)
    print(sys)
    
    time, yout, xout = sig.lsim(sys, U=np.zeros(1000), T=t, X0=[1, 0])

    plt.plot(time, yout, label="system response")
    plt.title("system repsonse")
    plt.xlabel("time")
    plt.ylabel("signal")
    plt.legend()
    plt.savefig("task7.1 system87a) system  response.pdf")
    plt.show()


    plt.plot(time, xout, label="state variables response")
    plt.title("state variable repsonse")
    plt.xlabel("time")
    plt.ylabel("signal")
    plt.legend()
    plt.savefig("task7.1 system87a) state variable  response.pdf")
    plt.show()


    time, stepresponse = sig.step(sys, T=t, X0=0)
    plt.plot(time, stepresponse, label="step response")
    plt.title("step response of system in taks 8.7")
    plt.xlabel("time")
    plt.ylabel("signal")
    plt.legend()
    plt.savefig("Task7.1 stepresponse.pdf")
    plt.show()
    
    
    time, totalresp = sig.step(sys, T=t, X0=[1, 0])
    plt.plot(time, stepresponse, label="step response")
    plt.title("total response of system in taks 8.7")
    plt.xlabel("time")
    plt.ylabel("signal")
    plt.legend()
    plt.savefig("Task7.1 totalresponse.pdf")
    plt.show()


system87()



