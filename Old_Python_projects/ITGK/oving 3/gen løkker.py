sum=0
for n in range(1,101):
    sum+=n
print(sum)

product=1
multiplier=2
while product<1000:
    product*=multiplier
    print(product)
    multiplier+=1
print(product)
ans=1
while ans !="yes":
    ans=input("does this annoy you? ")