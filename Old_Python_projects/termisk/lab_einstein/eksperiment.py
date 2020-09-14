import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import scipy.optimize as opt


def epsi(y):
    return y/(np.exp(y)-1)
def dQ(Temp0,Tempf,n):
    return 3*n*(Temp0*epsi(Etemp/Temp0)-Tempf*epsi(Etemp/Tempf))

def plot_from_file(file):
    table=np.loadtxt(file,delimiter=",")
    time=table.transpose()[0]
    mass=table.transpose()[1]
    plt.plot(time,mass,".")
    plt.show()
    return True
#plot_from_file("time-masstable.txt")
def linregress(file):
    table=np.loadtxt(file,delimiter=",")
    return stats.linregress(table)
print("total",linregress("time-masstable.txt"))
print("prealu",linregress("time-mass-prealu.txt"))
print("postalu",linregress("time-mass-post-alu.txt"))
def plot_from_regress(table1,table2):
    t=np.linspace(0,660,1000)
    slope1=table1[0]

    intersect1=table1[1]
    slope2 = table2[0]
    intersect2 = table2[1]-5.91
   # print(slope1,intersect1,slope2,intersect2)
    plt.plot(t,slope1*t+intersect1)
    plt.plot(t,slope2*t+intersect2)
    plt.show()
    return True

plot_from_regress(linregress("time-mass-prealu.txt"),linregress("time-mass-post-alu.txt"))
def dist_avg(table1,table2):
    t=np.linspace(306,360,10000)
    avg1=np.average(table1[0]*t+table1[1])
    avg2=np.average(table2[0]*t+table2[1]-5.91)
    return(avg1-avg2)
m=dist_avg(linregress("time-mass-prealu.txt"),linregress("time-mass-post-alu.txt"))
print(m)
L=2*10**2
print("dq",m*L)
def dq(Etemp):
    return (3 * 5.91/26.981538 *8.31446* (295 * (Etemp / 295)/(np.exp(Etemp / 295)-1) - 77 * (Etemp /77)/(np.exp(Etemp /77)-1))-m*L)
print(opt.fsolve(dq,280))









