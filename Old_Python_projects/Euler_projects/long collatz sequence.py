longest=0
length_max=0

for i in range(1000000):
    startpoint=i
    length=0
    while i>1:
        if i%2==1:
            i=3*i+1
            length+=1
        else:
            i=i//2
            length += 1
    if length>length_max:
        longest=startpoint

print (longest)