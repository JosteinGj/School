import sympy as sp

temp0=sp.symbols("temp0")
tempf=77
dm=sp.symbols("dm")
Etemp=sp.Function("Etemp")(temp0,dm)
eq=3*5.91/26.981538*(temp0*(Etemp/temp0)/(sp.exp(Etemp/temp0)-1)-tempf*(Etemp/tempf)/(sp.exp(Etemp/temp0)-1))-dm*2*100
print(sp.diff(eq,temp0))