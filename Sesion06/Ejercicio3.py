# -*- coding: utf-8 -*-
"""
Created on Mon Mar 10 16:46:26 2025

@author: UO299673
"""

import numpy as np
import matplotlib.pyplot as plt

def puntoFijo(g,x0,tol=1.e-6, maxiter=200):
    xk=x0
    xant=x0
    error=np.inf
    i=0
    gi=np.zeros(1)
    while tol<error and i<maxiter:
        xant=xk
        xk=g(xk)
        gi=np.append(gi, xk)
        error=np.abs(xk-xant)
        i+=1
    return xk, i, gi
        





def busquedaIncremental(f,a,b,n):
    x= np.linspace(a,b,n+1)
    intervalos = np.zeros((n,2))
    y=f(x)
    contador=0
    for i in range(n):
        if y[i]*y[i+1]<0:
            intervalos[contador, :] = x[i:i+2]
            contador+=1
    intervalos= intervalos[:contador,:]
    return intervalos
x=np.linspace(0, 1, 100)
f=lambda x: np.exp(-x)-x
a,b=0,1
bi = busquedaIncremental(f, a, b, 200)
g=lambda x: np.exp(-x)
y=lambda x: x
pf, i, gi = puntoFijo(g, bi[0][0])
print("Existe una raíz en ", bi)
print(pf, i)

plt.figure()
plt.plot(x, y(x), label="y = x")
plt.plot(x, g(x), label="g")
plt.plot(gi[-1], gi[-1], 'bo')
plt.show()


f2=lambda x: x-np.cos(x)
g1=lambda x:np.cos(x)
g2=lambda x: 2*x - np.cos(x)
g3=lambda x: x-((x-np.cos(x))/(1+np.sin(x)))
g4=lambda x: (9*x +np.cos(x))/10
bi= busquedaIncremental(f2, a, b, 200)
pf2, i2, gi2 = puntoFijo(g1, bi[0][0])
print("Existe una raíz en ", bi)
print("g1\t",pf2, i2)
pf2, i2, gi2 = puntoFijo(g2, bi[0][0])
print("g2\t",pf2, i2)
pf2, i2, gi2 = puntoFijo(g3, bi[0][0])
print("g3\t",pf2, i2)
pf2, i2, gi2 = puntoFijo(g4, bi[0][0])
print("g4\t",pf2, i2)
plt.figure()
plt.plot(x, g1(x))
plt.plot(x, g2(x))
plt.plot(x, g3(x))
plt.plot(x, g4(x))
plt.plot(gi2[-1], gi2[-1], 'bo')
plt.plot(x, y(x))
plt.xlim(0.0, 1.0)
plt.show()