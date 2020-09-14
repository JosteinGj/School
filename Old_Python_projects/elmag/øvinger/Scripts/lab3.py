import sympy as sp
import numpy as np
U,r,b,dU,dr,db=sp.symbols("U r b dU dr db")
difs=[dU,dr,db]
varsr=[U,r,b]
f=(2*U)/(r**2 *(b)**2)
parts=[]
for i in varsr:
    parts.append(sp.diff(f,i))
print (parts)
parts[0]*=difs[0]
parts[1]*=difs[1]
parts[2]*=difs[2]

substs=[]
for i in parts:
    substs.append(i.subs([(r,0.038),(b,7.5),(U,100),(dr,0.005),(db,0.15),(dU,0.5)]))
val=0
for i in substs:
    val+=i**2
print(val)
print(sp.sqrt(val))
print(sp.sqrt(val)/f.subs([(r,0.038),(b,7.5),(U,100)]))



