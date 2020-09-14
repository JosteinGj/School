import math
def f(x):
    return (x-12)*math.e**(5*x)-8*(x+2)**2
print(f(0))
def g(x):
    return -x-2*x**2-5*x**3+6*x**4
def derivate(0.0000001,x,func):
    print(func(x))
    return ((func(x+(h/2))-func(x-(h/2)))/2)

print(derivate(0,f))