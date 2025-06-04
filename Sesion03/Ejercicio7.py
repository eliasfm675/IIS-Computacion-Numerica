# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 15:30:09 2025

@author: uo299673
"""


import numpy as np
import matplotlib.pyplot as plt
import numpy.polynomial.polynomial as pol
np.set_printoptions(suppress = True)
def horner(x0, p):
    n = len(p)
    m=len(x0)
    q = np.zeros((m,n))
    q[:,-1] = p[-1]
    for i in range(n-2, -1, -1):
        q[:,i]=q[:,i+1]*x0+p[i]
    cociente = q[:,1:]
    resto = q[:,0]
    return cociente, resto

def derivadasSuc(x,p):
    m=len(x)
    n=len(p)
    y=np.zeros((m,n))
    P=np.copy(p)
    for i in range(n):
        P, y[:,i]=horner(x, P)
    return y
    
p = np.array([1., -1, 2, -3,  5, -2])
x = np.linspace(0, 1, 100)
y=derivadasSuc(x, p)
plt.figure()
plt.plot(x, y[:,0])
plt.plot(x, y[:,1])
plt.plot(x,y[:,2])
plt.plot(x, 0*x, 'k')
plt.legend()
