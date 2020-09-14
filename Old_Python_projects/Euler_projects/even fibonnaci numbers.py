n=input()
def evenfibonacci(n):
    a=1
    b=2
    fibs=[]
    EvenFibs=[]
    while a<n:
        fibs.append(a)
        fibs.append(b)

        a=a+b
        b=a+b
    print(fibs)
    for n in fibs:
        if n%2==0:
            EvenFibs.append(n)
    print(sum(EvenFibs))
    return EvenFibs
evenfibonacci(100000)
