def part1():
    nummber=int(input("skriv inn tall"))
    list=[]
    for n in range(1,nummber):
        if not n%2:
            list.append(-(n**2))
        else:
            list.append(n**2)
    print(list)
    print(sum(list))
k=int(input("øvre grense"))
nummber=int(input("skriv inn tall"))
list=[]
total=[]
counter=0
counter2=0
for n in range(1,nummber):
    counter+=1
    if not n%2:
        list.append(-(n**2))
    else:
        list.append(n**2)
    if sum(list) > k:
        break

for n in range(1,nummber):
    counter2+=1
    if not n%2:
        total.append(-(n**2))
    else:
        total.append(n**2)
print(counter)
print(list)
print (total)
print(sum(list[:-1:]))
print(sum(total))