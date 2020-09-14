def linecount(file):
    file=open(file)
    for i,l in enumerate(file):
        pass
    return i+1
print(linecount("numbers.txt"))
def numfreq(filename):
    file=open(filename)
    cont=list(file)
    content=[]
    dick={}
    for i in range(len(cont)):
        content.append(cont[i][0])
    print(content)
    for i in range(10):
        dick[i]=content.count(str(i))
    return dick
for key,val in numfreq("numbers.txt").items():
    print(key,":", val)

