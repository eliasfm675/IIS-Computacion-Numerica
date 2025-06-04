# -*- coding: utf-8 -*-
"""
Created on Mon Mar 17 15:58:27 2025

@author: UO299673
"""
import numpy as np
import numpy.polynomial.polynomial as pol
import matplotlib.pyplot as plt
def polinomio_lagrange(x,y,xp):
    n =len(x)
    yp=0.
    for i in range(n):
        yp+=y[i]*lagrange_fundamental(i, x, xp)
    return yp
def lagrange_fundamental(i,x,z):
    n =len(x)
    ypf=1.
    for k in range(n):
        if k!= i:
            ypf *= (z-x[k]) / (x[i]-x[k])
    return ypf

x = np.array([-1.,0,2,3,5])
y = np.array([1.,3,4,3,1])
x1 = np.array([-1.,0,2,3,5,6,7])
y1 = np.array([1.,3,4,3,2,2,1])
p = pol.polyfit(x,y,len(x)-1)  # coeficientes del polinomio
xp = np.linspace(min(x),max(x))
yp = pol.polyval(xp,p)
yz = polinomio_lagrange(x, y, xp)
plt.figure()
plt.plot(xp, yp, '-',x,y,'o')
plt.title("Using polyval y polyfit")
plt.show()

plt.figure()
plt.plot(xp, yz, '-',x,y,'o')
plt.title("Using polinomio_langrange(x,y)")
plt.show()

xp= np.linspace(min(x1),max(x1))
yz=polinomio_lagrange(x1, y1, xp)
print(yz)
plt.figure()
plt.plot(xp, yz, '-',x1,y1,'ro')
plt.title("Using polinomio_langrange(x1,y1)")
plt.show()