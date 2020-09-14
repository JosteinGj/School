def f(x):
def g(x):
def derivate(h,x,func):
def newtons method(h,x,func,tol):
    dx=tol+1
    x_new=x
    while dx>=tol:
        x_old=x_new
        x_new=x_old - func(x_old)/derivate(h,x,func)
        dx=abs(x_old-x_new)
    return x_new
