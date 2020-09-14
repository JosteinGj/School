import math
def gcd(a,b):
    return math.gcd(a,b)
def ektegcd(a,b):
    while b !=0:
        temp=b
        b=a%b
        a=temp
        return a
def reduce_faction(a,b):
    d=ektegcd(a,b)
    return "%s/%s" % (a//d,b//d)
print(reduce_faction(144,8))
