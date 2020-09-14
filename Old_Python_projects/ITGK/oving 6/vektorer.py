import math

def vectorify(a,b,c):
    return list((a,b,c))

def skalar_multiplikasjon(c,v):
    result=[]
    for ind in v:
        result.append(ind*c)
    return result
def vektorlengde(v):
    result=[]
    for n in v:
        result.append(n**2)
    return math.sqrt(sum(result))
vec2=[2,3,4]
print(skalar_multiplikasjon(2,vec2))
print(vektorlengde(vec2),vektorlengde(skalar_multiplikasjon(2,vec2)))
print(vektorlengde(skalar_multiplikasjon(2,vec2))/vektorlengde(vec2))
def prikk_product(v,u):
    result=[]
    for n in range(len(v)):
        result.append(v[n]*u[n])
    return result
print(prikk_product(vec2,vec2))