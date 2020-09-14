a=int(input("sum opp til:"))
r=float(input("skriv et tall mellom -1 og 1"))
partial_sums=[]
tol=float(input("tolleranse"))

def part1(a,r):
    counter=0
    for num in range(0,a+1):
        counter+=1
        partial_sums.append(r**num)
        total=sum(partial_sums)
        if total-(1/(1-r))>=tol:
            break
def part2(r,tol):
    b=0
    partialSum=[]
    total=0
    while abs(total-(1/(1-r)))>=tol:
       partialSum.append(r**b)
       b+=1
       total=sum(partialSum)
    print(total)
    print(total-(1/1-r))
part2(r,tol)