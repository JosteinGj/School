def nested_loop():
    for a in range(1,5):
        print(a, "gangen")
        for b in range(1,5):
            print(a*b)

def primtall(n):
    limit=n
    primes=[True]*limit
    primes[0],primes[1]=[None]*2
    output=[]
    for ind,val in enumerate(primes):
        if val==True:
            primes[ind*2::ind]=[False]*(((limit-1)//ind)-1)
            output.append(ind)
    return output
print(primtall(100))