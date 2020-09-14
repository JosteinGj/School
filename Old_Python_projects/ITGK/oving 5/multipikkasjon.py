def func(tol):
    prod=1
    a=1
    counter=0
    while prod-(prod/(1+(1/a**2)))>tol:
        print(prod)
        prod *= (1 + (1 / a ** 2))
        a+=1
        counter+=1
    return prod, counter
print(func(0.01))
