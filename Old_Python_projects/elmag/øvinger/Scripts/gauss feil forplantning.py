import numpy as np
from numpy import sqrt
import scipy.constants as sci
import sympy
import matplotlib.pyplot as plt

x,I,R,mu,N,a,L,dx,dI,dR,da,dL = sympy.symbols("x I R mu N a L dx dI dR da dL")

kortspole=((N*mu*I)/(2*R)*(1+(x/R)**2)**(-1.5)*10**4)

helmholtz=(((N*mu*I)/(2*R))*(((1+((x-(a/2))/R)**2)**(-1.5)+(1+((x+(a/2))/R)**2)**(-1.5))))*10**4
#(((N*mu*I)/(2*R))*(((1+(x-(a/2))/R)**2)**(-1.5)+(1+(x+(a/2)/R)**2)**(-1.5)*10**4))

solenoide=(((N*mu*I)/(2*L))*(x/sympy.sqrt(x**2+R**2)+((L-x)/sympy.sqrt((L-x)**2+R**2))))*10**4
#(((N*mu*I)/2*L)*(x/sympy.sqrt(x**2+R**2)-(L-x)/sympy.sqrt((L-x)**2+R**2))*10**4)
kortvars=[x,I,R]
helmvars=[x,I,R,a]
solvars=[x,I,R,L]

def partdiff(f,variables):
    output=[]
    for var in variables:
        output.append(sympy.diff(f,var))
    return output

part_kort=partdiff(kortspole,kortvars)
part_helm=partdiff(helmholtz,helmvars)
part_sol=partdiff(solenoide,solvars)

part_kort[0]*=dx
part_kort[1]*=dI
part_kort[2]*=dR
part_helm[0]*=dx
part_helm[1]*=dI
part_helm[2]*=dR
part_helm[3]*=da
part_sol[0]*=dx
part_sol[1]*=dI
part_sol[2]*=dR
part_sol[3]*=dL

kort_subs=[]
helm_subs=[]
sol_subs=[]
for func in part_kort:
    kort_subs.append((func).subs([(I,0.75),(R,0.07),(N,330),(mu,sci.mu_0),(dx,0.0005),(dI,0.02125),(dR,0.0005),(dL,0.001),(da,0.0015)]))

for func in part_helm:
    helm_subs.append((func).subs([(I,0.75),(R,0.07),(N,330),(mu,sci.mu_0),(a,0.14),(dx,0.0005),(dI,0.02125),(dR,0.0005),(dL,0.001),(da,0.0015)]))


#helmholtz_B=(((N*mu*I)/(2*R))*(((1+((x-(a/2))/R)**2)**(-1.5)+(1+((x+(a/2))/R)**2)**(-1.5))))*10**4
#helmholtz_2r_B.subs([(I,0.75),(R,0.07),(N,330),(mu,sci.mu_0),(a,0.14),(dx,0.0005),(dI,0.02125),(dR,0.0005),(dL,0.001),(da,0.0015)])

dkort_sqrd=0
dhelm_sqrd=0
dsol_sqrd=0
for func in kort_subs:

    dkort_sqrd+=func**2
for func in part_sol:
    sol_subs.append((func).subs([(I,0.67),(R,0.05),(N,368),(mu,sci.mu_0),(L,0.39),(dx,0.0005),(dI,0.02125),(dR,0.0005),(dL,0.001),(da,0.0015)]))

dkort=sympy.sqrt(dkort_sqrd)
for func in helm_subs:
    dhelm_sqrd+=func**2
dhelm=sympy.sqrt(dhelm_sqrd)
for func in sol_subs:
    dsol_sqrd+=func**2
dsol=sympy.sqrt(dsol_sqrd)

#print("dkort: ", dkort,"\n")
#print("dhelm: ",dhelm,"\n")
#print("dsol: ", dsol,"\n")
x=np.linspace(-0.3,0.3,1000)
pos=np.linspace(-0.3,0.3,1000)
solpos=np.linspace(-0.1,0.5,1000)

kort_målt=np.loadtxt("kort_målt_B.txt",skiprows=1)
r_2_målt=np.loadtxt("Helm_R-2_målt.txt",skiprows=1)
r_målt=np.loadtxt("Helm_r_målt.txt",skiprows=1)
r2_målt=np.loadtxt("Helm_2r_målt.txt",skiprows=1)
sol_målt=np.loadtxt("sol_målt.txt",skiprows=1)
r2diff=np.loadtxt("2rdiff.txt",skiprows=1)
helmpos_2r=np.loadtxt("diffposs2r.txt",skiprows=1)
rdiff=np.loadtxt("helmholtz_diff_a_r.txt",skiprows=1)
helmpos_R=np.loadtxt("pointposhelm_A_R.txt",skiprows=1)
helmpos_R_2=np.loadtxt("pos_a_r_2.txt",skiprows=1)
diffr_2=np.loadtxt("diff_r_2.txt",skiprows=1)
solpos=np.loadtxt("solenoidpos.txt",skiprows=1)
soldiff=np.loadtxt("soldiff.txt",skiprows=1)
kortdiff=np.loadtxt("diffkort.txt",skiprows=1)
kortpos=np.loadtxt("kortpos.txt",skiprows=1)

helm_x=(((330*sci.mu_0*0.75)/(2*0.07))*(((1+((pos-(0.07/2))/0.07)**2)**(-1.5)+(1+((pos+(0.07/2))/0.07)**2)**(-1.5))))*10**4

#pos=kortpos
#x=kortpos
uncert_kort=sqrt(46.2492209143135*x**2*(204.081632653061*x**2 + 1)**(-5.0) + 0.396195378407557*(204.081632653061*x**2 + 1)**(-3.0) + (97.1525424943949*x**2*(204.081632653061*x**2 + 1)**(-2.5) - 0.158682486074178*(204.081632653061*x**2 + 1)**(-1.5))**2)
rel_uncert_kort=uncert_kort*100/((330*sci.mu_0*0.75)/(2*0.07)*(1+(pos/0.07)**2)**(-1.5)*10**4)

#x=helmpos_2r
#pos=helmpos_2r
uncert_helm_2R=sqrt((-10.2010169619115*(-x + 0.07)*(204.081632653061*(x - 0.07)**2 + 1)**(-2.5) - 10.2010169619115*(x + 0.07)*(204.081632653061*(x + 0.07)**2 + 1)**(-2.5))**2 + (-3.40033898730382*(2*x - 0.14)*(204.081632653061*(x - 0.07)**2 + 1)**(-2.5) - 3.40033898730382*(2*x + 0.14)*(204.081632653061*(x + 0.07)**2 + 1)**(-2.5))**2 + (0.629440528094241*(204.081632653061*(x - 0.07)**2 + 1)**(-1.5) + 0.629440528094241*(204.081632653061*(x + 0.07)**2 + 1)**(-1.5))**2 + (97.1525424943949*(x - 0.07)**2*(204.081632653061*(x - 0.07)**2 + 1)**(-2.5) + 97.1525424943949*(x + 0.07)**2*(204.081632653061*(x + 0.07)**2 + 1)**(-2.5) - 0.158682486074178*(204.081632653061*(x - 0.07)**2 + 1)**(-1.5) - 0.158682486074178*(204.081632653061*(x + 0.07)**2 + 1)**(-1.5))**2)
rel_uncert_helm_2R=uncert_helm_2R*100/((((330*sci.mu_0*0.75)/(2*0.07))*(((1+((pos-(0.07/2))/0.07)**2)**(-1.5)+(1+((pos+(0.07/2))/0.07)**2)**(-1.5))))*10**4)

#x=helmpos_R
#pos=helmpos_R
uncert_helm_R=sqrt((-10.2010169619115*(-x + 0.035)*(204.081632653061*(x - 0.035)**2 + 1)**(-2.5) - 10.2010169619115*(x + 0.035)*(204.081632653061*(x + 0.035)**2 + 1)**(-2.5))**2 + (-3.40033898730382*(2*x - 0.07)*(204.081632653061*(x - 0.035)**2 + 1)**(-2.5) - 3.40033898730382*(2*x + 0.07)*(204.081632653061*(x + 0.035)**2 + 1)**(-2.5))**2 + (0.629440528094241*(204.081632653061*(x - 0.035)**2 + 1)**(-1.5) + 0.629440528094241*(204.081632653061*(x + 0.035)**2 + 1)**(-1.5))**2 + (97.1525424943949*(x - 0.035)**2*(204.081632653061*(x - 0.035)**2 + 1)**(-2.5) + 97.1525424943949*(x + 0.035)**2*(204.081632653061*(x + 0.035)**2 + 1)**(-2.5) - 0.158682486074178*(204.081632653061*(x - 0.035)**2 + 1)**(-1.5) - 0.158682486074178*(204.081632653061*(x + 0.035)**2 + 1)**(-1.5))**2)
rel_uncert_helm_R=uncert_helm_R*100/((((330*sci.mu_0*0.75)/(2*0.07))*(((1+((pos-(0.07/2))/0.07)**2)**(-1.5)+(1+((pos+(0.07/2))/0.07)**2)**(-1.5))))*10**4)

#x=helmpos_R_2
#pos=helmpos_R_2
uncert_helm_R_2=sqrt((-10.2010169619115*(-x + 0.0185)*(204.081632653061*(x - 0.0185)**2 + 1)**(-2.5) - 10.2010169619115*(x + 0.0185)*(204.081632653061*(x + 0.0185)**2 + 1)**(-2.5))**2 + (-3.40033898730382*(2*x - 0.037)*(204.081632653061*(x - 0.0185)**2 + 1)**(-2.5) - 3.40033898730382*(2*x + 0.037)*(204.081632653061*(x + 0.0185)**2 + 1)**(-2.5))**2 + (0.629440528094241*(204.081632653061*(x - 0.0185)**2 + 1)**(-1.5) + 0.629440528094241*(204.081632653061*(x + 0.0185)**2 + 1)**(-1.5))**2 + (97.1525424943949*(x - 0.0185)**2*(204.081632653061*(x - 0.0185)**2 + 1)**(-2.5) + 97.1525424943949*(x + 0.0185)**2*(204.081632653061*(x + 0.0185)**2 + 1)**(-2.5) - 0.158682486074178*(204.081632653061*(x - 0.0185)**2 + 1)**(-1.5) - 0.158682486074178*(204.081632653061*(x + 0.0185)**2 + 1)**(-1.5))**2)
rel_uncert_helm_R_2=uncert_helm_R_2*100/((((330*sci.mu_0*0.75)/(2*0.07))*(((1+((pos-(0.07/2))/0.07)**2)**(-1.5)+(1+((pos+(0.07/2))/0.07)**2)**(-1.5))))*10**4)
solpos=np.linspace(-0.1,0.5,1000)
x=solpos
uncert_sol=sqrt((-9.93065493165512e-5*x/(x**2 + 0.0025)**(3/2) - 9.93065493165512e-5*(-x + 0.39)/((-x + 0.39)**2 + 0.0025)**(3/2))**2 + (0.125985920774729*x/sqrt(x**2 + 0.0025) + 0.125985920774729*(-x + 0.39)/sqrt((-x + 0.39)**2 + 0.0025))**2 + (-0.0101852871093899*x/sqrt(x**2 + 0.0025) + 0.00397226197266205*(-x + 0.39)*(x - 0.39)/((-x + 0.39)**2 + 0.0025)**(3/2) - 0.0101852871093899*(-x + 0.39)/sqrt((-x + 0.39)**2 + 0.0025) + 0.00397226197266205/sqrt((-x + 0.39)**2 + 0.0025))**2 + (-0.00198613098633102*x**2/(x**2 + 0.0025)**(3/2) + 0.00198613098633102*(-x + 0.39)**2/((-x + 0.39)**2 + 0.0025)**(3/2) - 0.00198613098633102/sqrt((-x + 0.39)**2 + 0.0025) + 0.00198613098633102/sqrt(x**2 + 0.0025))**2)
rel_uncert_sol=uncert_sol*100/((((330*sci.mu_0*0.67)/(2*0.39))*(solpos/sqrt(solpos**2+0.05**2)+((0.39-solpos)/sqrt((0.39-solpos)**2+0.05**2))))*10**4)
x=np.linspace(-0.3,0.3,1000)
pos=helmpos_R
sol=(((368*sci.mu_0*0.67)/(2*0.39))*(solpos/sqrt(solpos**2+0.05**2)+((0.39-solpos)/sqrt((0.39-solpos)**2+0.05**2))))*10**4
helm_r=(((330*sci.mu_0*0.75)/(2*0.07))*(((1+((pos-(0.07/2))/0.07)**2)**(-1.5)+(1+((pos+(0.07/2))/0.07)**2)**(-1.5))))*10**4
solpos=np.loadtxt("solenoidpos.txt",skiprows=1)
solposx=np.linspace(-0.1,0.5,1000)

yerror_kort= ((kort_målt*0.004+0.1+0.001)*100)/kort_målt
yerror_r= ((r_målt*0.004+0.1+0.001)*100)/r_målt
yerror_2r= ((r2_målt*0.004+0.1+0.001)*100)/r2_målt
yerror_r_2= ((r_2_målt*0.004+0.1+0.001)*100)/r_2_målt
yerror_sol=((sol_målt*0.004+0.1+0.001)*100)/sol_målt


#print((sum(rel_uncert_helm_R_2)+sum(rel_uncert_helm_R)+sum(rel_uncert_helm_2R)+sum(rel_uncert_sol)+sum(rel_uncert_kort))/(sum([len(kortpos),len(helmpos_R_2),len(helmpos_R),len(helmpos_2r),len(solpos)])))
#print(part_kort)
def plot_sol():
    plt.plot(solposx*100,rel_uncert_sol,color="black",label="Relativ usikkerhet fra Gauss")
    plt.plot(solposx * 100, -rel_uncert_sol,color="black")
    plt.errorbar(solpos*100,soldiff,yerr=yerror_sol,fmt=".",label="Måleusikkerhet i gaussmeteret",color="r")
    plt.plot(solpos*100,soldiff,".",label="Avvik fra beregnet verdi",color="r")
    plt.xlabel("Koaksial avstand fra venstre ende av spolen (cm)")
    plt.ylabel("Avvik/usikkerhet (%)")
    plt.legend()
    plt.grid()
    plt.savefig("sol_uncert_v3.pdf", bbox_inches="tight",pad_inches=0)
    plt.show()
#plot_sol()


#kortdiff=np.loadtxt("diffkort.txt",skiprows=1)
#kortpos=np.loadtxt("kortpos.txt",skiprows=1)
#x=kortpos
def plot_kort():
    plt.plot(x*100,rel_uncert_kort,color="black",label="Relativ usikkerhet fra Gauss")
    plt.plot(x * 100, -rel_uncert_kort,color="black")
    plt.plot(kortpos*100,kortdiff,".",label="Avvik fra beregnet verdi",color="r")
    plt.errorbar(kortpos*100,kortdiff,fmt=".",yerr=yerror_kort,label="Måleusikkerhet i gaussmeteret",color="r")
    plt.xlabel("Koaksial avstand fra senter av spole (cm)")
    plt.ylabel("Avvik/usikkerhet (%)")
    plt.legend()
    plt.grid()
    plt.savefig("kort_uncert_v3.pdf", bbox_inches="tight",pad_inches=0)
    plt.show()
#plot_kort()

def plot_helm():
    fig,(ax1,ax2,ax3)=plt.subplots(nrows=3,ncols=1)
    plt.subplots_adjust(hspace=1)

    ax1=plt.subplot(3,1,2)
    ax1.plot(x*100,rel_uncert_helm_2R,label="Usikkerhet fra Gauss",color="black")
    ax1.plot(x * 100,-rel_uncert_helm_2R,color="black")
    ax1.plot(helmpos_2r*100,r2diff,".",label="Avvik fra beregnet verdi",color="r")
    ax1.errorbar(helmpos_2r * 100, r2diff, fmt=".", yerr=yerror_2r, label="Måleusikkerhet i gaussmeteret",color="r")
    plt.title("a=2R")
    plt.xlabel("Koaksial avstand fra sentrum av spolene (cm)")
    plt.ylabel("Avvik/Usikkerhet (%)")
    plt.grid()

    ax2 = plt.subplot(3, 1, 1)
    ax2.plot(x*100,rel_uncert_helm_R,label="Usikkerhet fra gauss",color="black")
    ax2.plot(x * 100,-rel_uncert_helm_R,color="black")
    ax2.plot(helmpos_R*100,rdiff,".",label="Avvik fra beregnet verdi",color="r")
    ax2.errorbar(helmpos_R * 100, rdiff, fmt=".", yerr=yerror_r, label="Måleusikkerhet i gaussmeteret",color="r")

    plt.title("a=R")
    plt.xlabel("Koaksial avstand fra sentrum av spolene (cm)")
    plt.ylabel("Avvik/Usikkerhet (%)")
    plt.grid()

    ax3=plt.subplot(3,1,3)
    ax3.plot(x*100,rel_uncert_helm_R_2,label="Usikkerhet fra gauss",color="black")
    ax3.plot(x * 100,-rel_uncert_helm_R_2,color="black")
    ax3.plot(helmpos_R_2*100,diffr_2,".",label="Avvik fra beregnet verdi",color="r")
    ax3.errorbar(helmpos_R_2 * 100, diffr_2, fmt=".", yerr=yerror_r_2, label="Måleusikkerhet i gaussmeteret",color="r")
    plt.title("a=37mm")
    plt.xlabel("Koaksial avstand fra sentrum av spolene (cm)")
    plt.ylabel("Avvik/Usikkerhet (%)")
    plt.grid()
    fig.set_size_inches(8.5,8.5,forward=True)
    ax1.legend(bbox_to_anchor=[0.6, 1],loc="best")

    plt.savefig("helm_uncert_v7.pdf", bbox_inches="tight", pad_inches=0)

    plt.show()
plot_helm()
#r2diff=np.loadtxt("2rdiff.txt",skiprows=1)
#diffpos_2r=np.loadtxt("diffposs2r.txt",skiprows=1)
#rdiff=np.loadtxt("helmholtz_diff_a_r.txt",skiprows=1)
#diffpos_R=np.loadtxt("pointposhelm_A_R.txt",skiprows=1)
#diffpos_R_2=np.loadtxt("pos_a_r_2.txt",skiprows=1)
#diffr_2=np.loadtxt("diff_r_2.txt",skiprows=1)

#fig,(ax1,ax2,ax3)=plt.subplots(nrows=3,ncols=1)
#plt.subplots_adjust(hspace=1)
#ax1=plt.subplot(3,1,1)

#ax1.plot(pos*100,rel_uncert_helm_R,label="rel")
#ax1.plot(diffpos_R*100,rdiff,".",label="avvik")
#plt.grid()
#plt.title("a=R")
#plt.xlabel("avstand fra spole (cm)")
#plt.ylabel("usikkerhet (%)")


#ax2=plt.subplot(3,1,2)
#ax2.plot(pos*100,rel_uncert_helm_2R,label="rel")
#plt.grid()
#plt.title("a=2R")
#ax1.set_ylim(-2,7)
#ax2.plot(diffpos_2r*100,r2diff,".",label="avvik")
#plt.xlabel("avstand fra spole (cm)")
#plt.ylabel("usikkerhet (%)")


#ax3=plt.subplot(3,1,3)
#ax3.plot(pos*100,rel_uncert_helm_R_2,label="Rel")
#plt.grid()
#ax3.plot(diffpos_R_2*100,diffr_2,".",label="avvik")
#plt.ylim(-6,6)
#plt.title("a=R/2")
#plt.xlabel("avstand fra spole (cm)")
#plt.ylabel("usikkerhet (%)")
#plt.figlegend((ax1,ax2),("målt","text"),bbox_to_anchor=[0.9, 0.88], loc='upper right')
#plt.savefig("helmholtz_uncert.pdf", bbox_inches="tight",pad_inches=0)
#plt.show()
