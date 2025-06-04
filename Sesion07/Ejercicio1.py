# -*- coding: utf-8 -*-
"""
Created on Mon Mar 17 15:12:27 2025

@author: UO299673
"""
import matplotlib.pyplot as plt
import numpy as np
def lagrange_fundamental(i,x,z):
    n =len(x)
    ypf=1.
    for k in range(n):
        if k!= i:
            ypf *= (z-x[k]) / (x[i]-x[k])
    return ypf

x = np.array([-1.,0,2,3,5])
n =len(x)
xp = np.linspace(min(x),max(x),100)
#z = np.array([1.3, 2.1, 3.2])
z=xp
y0=np.eye(n)
print(y0)
for i in range(n):
   ypf = lagrange_fundamental(i, x, z)
   plt.figure()
   plt.plot(xp, ypf)
   plt.plot(x, 0*x, 'k')
   plt.plot(x, y0[i], 'ro')
   plt.title("L"+str(i))
   plt.show()
