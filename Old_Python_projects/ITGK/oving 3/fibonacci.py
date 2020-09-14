n=int(input("hvor mange fibonacci tall vil du skrive ut?"))
def fibonacci(n):
    a=0
    b=1
    fibs=[]
    while len(fibs)<= n:
        fibs.append(a)
        if len(fibs)<=n:
            fibs.append(b)
        a=a+b
        b=a+b
    print(fibs)
    print(fibs[-1])
    print(sum(fibs))
fibonacci(n)
