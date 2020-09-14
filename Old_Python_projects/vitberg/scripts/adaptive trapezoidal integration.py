


# Computes approximation of definite integral
# Inputs: Function f , interval[a,b], tolerance
# Output: approximate integral


# Returns a single trapezoid
def trap(f,a,b):
    return ((f(a)+f(b))*(b-a))/2


def adaptive_trap(f,start,end,tol0):
    integral=0
    app=[trap(f,start,end)]
    a=[start]
    b=[end]
    tol=[tol0]
    n=1
    while n>0:
        pivot=(a+b)/2
        oldapp=app[-1]
        app[-1]=trap(f,a,pivot)
        app.append(trap(f,pivot,b))
        if abs(oldapp-(app[-1]+app[-2]))<3*tol:
            integral+=(app[-1]+app[-2])
            n=n-1
        else:
            b.append(b)



