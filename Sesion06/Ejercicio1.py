# -*- coding: utf-8 -*-
"""
Created on Mon Mar 10 15:14:16 2025

@author: UO299673
"""
import numpy as np
import matplotlib.pyplot as plt
def secante(f,x0,x1,tol=1.e-6, maxiter=100):
    error=np.inf
    i=0
    x=x1
    xant=x0
    while error>tol and i<maxiter:
        temp=x
        x=x-f(x)*((x-xant)/(f(x)-f(xant)))
        xant=temp
        error=np.abs(x-xant)
        i+=1
    return x,i
f= lambda x: x**5 -3*x**2 +1.6
x0=-1
x1=-0.1
r = np.zeros(0)
r = np.append(r, secante(f, x0, x1) )
x2=0.5
x3=1
x4=1.2
x5=1.5
r = np.append(r, secante(f, x2, x3) )
r = np.append(r, secante(f, x4, x5) )
x=np.linspace(-1, 1.5, 100)
print(r)
plt.figure()
plt.plot(r, r*0, 'ro')
plt.plot(x, f(x))
plt.plot(x, x*0, 'k')
plt.xlim(-1.0, 1.5)
plt.show()