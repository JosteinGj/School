def seperate(num,tol):
    supercrit=[]
    subcrit=[]
    for n in num:
        if n<tol:
            subcrit.append(n)
        else:
            supercrit.append(n)
    return  subcrit, supercrit


def multiplication_table(n):
    matrix= list(list(range(i,(n+1)*i,i)) for i in range(1,n+1))
    return matrix
table=multiplication_table(1000)
for i in range(len(table)):
    print (table[i])
