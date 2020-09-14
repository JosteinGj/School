import numpy as np
from operator import mul
import functools as ft
def f0(x):return x
def f1():return 1
X=range(4)
def coef(k,f0):
    sJ=0
    if k==0:
        return f0(X[0])
    for i in range(k):
        sJ=+coef(i,f0)