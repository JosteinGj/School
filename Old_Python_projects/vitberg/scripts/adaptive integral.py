import math as m

count=0
def f(x):return x**3+x**2+x+1
def g(x): return m.exp(x)/m.cos(x)


def trap(f,a,b):
    return ((f(a)+f(b))*(b-a))/2


def adaptive_int(f,a,b,tol):
    integral=0
    p=(a+b)/2
    app=trap(f,a,b)
    app_ap=trap(f,a,p)
    app_pb=trap(f,p,b)

    if abs(app-(app_ap+app_pb))<3*tol:
        integral +=(app_ap+app_pb)
        return integral
    else:
         integral+=adaptive_int(f,a,p,tol/2)+adaptive_int(f,p,b,tol/2)
         return integral

#print(adaptive_int(g,0,1,1e-8),"count=",count)
print( "integral of g from 2*sqrt(2*pi) to 5= ",adaptive_int(f,0,2*m.sqrt(2*m.pi),1e-7))
count=0
print( "integral of g from 2*sqrt(2*pi) to 5= ",adaptive_int(f,2*m.sqrt(2*m.pi),5,1e-7))

