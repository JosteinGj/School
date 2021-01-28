import numpy as np
import scipy as sci
import matplotlib.pyplot as plt


g=9.81
l=1
def euler(dt,w,theta):
    dtheta = w * dt
    dw = (-g/l)*theta*dt
    w += dw
    theta += dtheta
    return w, theta


def lol_rip(theta_0=0.2, w_0=0, t0=0, ts=10, m=5):
    #lag liste med tidsteg
    dts = [0.001, 0.004, 0.007]
    
    
    # analytisk løsning
    anal_time = np.linspace(t0, ts, 100000)
    anal_theta = theta_0 * np.cos(np.sqrt(g / l) * anal_time)


    # plott inni for løkke for å imponere damene
    for dt in dts: # imponer damene
        theta, w, t = theta_0, w_0, t0
        thetas, ws, times = [theta_0], [w_0], [t0]
        while(t < ts):
            w, theta = euler(dt, w, theta)
            t += dt
            times.append(t)
            thetas.append(theta)
            ws.append(w)
        # plot dritten    
        plt.plot(times, thetas, label=f"solution dt={dt}")
        # plot analen dritten kom fra
        plt.plot(anal_time, anal_theta, label="anal solution")
        
        # pynt på det, du ska kanskje vise denne dritten te någen
        plt.xlabel("Time [s]")
        plt.ylabel(r"$\theta$ [rad]")
        plt.legend(loc="upper left")
        plt.title(f"num sol dt={dt}")
        
        # lagre dritten så du finne den igjen
        plt.savefig(f"anal_num_comp_dt={dt}.pdf")
        plt.show()

        thetas = np.array(thetas)
        ws = np.array(ws)
        times = np.array(times)

        E_p = 0.5 * m * l * g * thetas ** 2 # mlg pro gamer moves to impress the ladies. 
        E_k = 0.5 * m * l ** 2 * ws ** 2 
        E = E_k + E_p
        plt.plot(times, E)
        # mekk pynt her

        plt.show()

        


        

lol_rip()





    
