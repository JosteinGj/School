import random
list1=[]
for n in range(100):
    list1.append(random.randrange(1,11))
print(list1)
print(list1.count(2))
print(sum(list1))
print(sorted(list1))
counts=[]
for n in range(11):
    counts.append(list1.count(n))
print(max(counts))
print(list1[::-1])