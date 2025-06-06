# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 15:08:03 2025

@author: UO299673
"""
import numpy as np
import matplotlib.pyplot as plt
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
f1=lambda x: x**5 -3*x**2 +1.6
f2=lambda x: (x+2)*np.cos(2*x)
a=-1
b=1.5
c=0
d=10
n1=25
n2=100
print("Intervalos que contienen raíces de f1")
print(busquedaIncremental(f1, a, b, n1))
print("Intervalos que contienen raíces de f2")
print(busquedaIncremental(f2, c, d, n2))