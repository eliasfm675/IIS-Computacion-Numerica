# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 16:24:31 2025

@author: UO299673
"""

import numpy as np
import matplotlib.pyplot as plt
f = lambda x: np.exp(x)
tol=1.e-8
maxNumSum = 100
x=np.linspace(-1,1, 50)
def funExp(x,tol, maxNumSum):
    polinomio=0
    sumando=1
    factorial=1
    i=0
    while np.max(np.abs(sumando)) > tol and i+1<=maxNumSum:
        sumando=(x**i)/factorial
        polinomio+=sumando
        factorial*=i+1
        i+=1
    return polinomio
Ox=0*x
plt.figure()
plt.plot(x, Ox, 'k')
plt.plot(x, f(x), 'y', linewidth = 4 ,  label="f")
plt.plot(x, funExp(x,tol,maxNumSum), 'b--', label="funExp(x)")
plt.legend()
plt.title("Aproximación de f con el polinomio de McLaurin")
plt.show()