import numpy as np
import matplotlib.pyplot as plt

def func1(t,y):
   func=np.array([y[1],-4*y[0]])
   return func

def brusselator(t,y):
    return np.array([1+(y[0]**2)*y[1]-4*y[0],3*y[0]-3*y[0]-(y[0]**2)*y[1]])
def new_h(a,h,est,tol):
    return a*h*np.sqrt(tol/est)

def solver(t0,tend,y0,f,h0,tol):
    h=h0
    k=0
    t=[t0]
    y=[y0]
    throws=0
    fevals=1
    #print(y)
    f1=f(t0,y0)
   # print("f1",f1)
    while tend-t[k]:
        h=min(h,tend-t[k])
        t.append(t[k]+h)
        #print("tk",t[k])
        f2=f(t[k+1],y[k]+h*f1)
        fevals+=1
        #print("f1",f1)
       # print("f2",f2)

        y.append(y[k]+h*(f1+f2)/2)
        #print(y[k])
        print("tk",t[k])
      #  print(h*(f1-f2)/2)
        est=np.linalg.norm(h*(f1-f2)/2)
       # print("est",est)
        if est<tol:
            k=k+1
            #print("t",t)
           # print ("y",y)
            f1=f(t[k],y[k])
            fevals+=1
        else:
            throws+=1
            y.pop()
            t.pop()
        print(h)
        h=new_h(0.9,h,est,tol)
        print(h)
    stats=[len(t)-1,fevals,throws]
    return t,y,stats
#time1,y1,stats1 = solver(0,2*np.pi,[1,0],func1,0.1,10**-4)
time2,y2,stats2=solver(0,20,[1,2.9],brusselator,0.1,10**-3)
print(stats2)


