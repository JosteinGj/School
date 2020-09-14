lønninger=[[300,"diego"],[0,"mohammed"]]
def lønning(lønn, navn,lønninger):
    list1=[lønn,navn]
    lønninger.append(list1)
lønning(3000,"nora",lønninger)




n=10
table=[]
for i in range(1,n+1):
    table.append(list(range(i,(n+1)*i,i)))

for a in table:
    print(a)
