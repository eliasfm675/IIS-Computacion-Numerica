# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 15:30:09 2025

@author: uo299673
"""


import numpy as np
import matplotlib.pyplot as plt
import numpy.polynomial.polynomial as pol
def horner(x0, p):
    n = len(p)
    q = np.zeros(n)
    q[-1] = p[-1]
    for i in range(n-2, -1, -1):
        q[i]=q[i+1]*x0+p[i]
    cociente = q[1:]
    resto = q[0]
    return cociente, resto
p0 = np.array([1.,2,1])
x0=1.
c, r = horner(x0,p0)

p1=np.array([1.,-1,2,-3,5,-2])
x1=1.

p2= np.array([1.,-1,-1,1,-1,0,-1,1])
x2=-1.
print("Coeficientes de Q = ", c)
print("P0(1)       = ", r)
print("Con polyval = ", pol.polyval(x0,p0))

c, r = horner(x1,p1)
print("\n\n")

print("Coeficientes de Q = ", c)
print("P1(1)       = ", r)
print("Con polyval = ", pol.polyval(x1,p1))

c, r = horner(x2,p2)
print("\n\n")

print("Coeficientes de Q = ",c)
print("P0(1)       = ", r)
print("Con polyval = ", pol.polyval(x2,p2))
