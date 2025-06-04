# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 16:34:30 2025

@author: UO299673
"""

import numpy as np
import matplotlib.pyplot as plt
f = lambda x: np.sin(x)
tol=1.e-8
maxNumSum=100
x0=np.pi/4
def McL(x, tol, maxNumSum):
    factorial=1
    sumando=1
    polinomio=0
    i=1
    operacion=True
    while np.abs(sumando)>tol and i+1<=maxNumSum:   
        sumando=np.all((x**i)/factorial)
        if operacion:
            polinomio+=sumando
            operacion=False
        else:
            polinomio-=sumando
            operacion=True
        factorial*=i+2
        i+=2
    return  polinomio
x = np.linspace(-np.pi, np.pi, 50)
Ox=0*x
McL_vectorized = np.vectorize(McL)
plt.figure()
plt.plot(x, f(x), 'y', linewidth = 4 ,label="f")
plt.plot(x, McL_vectorized(x,tol,maxNumSum), 'b--', label="Aproximación de f")
plt.plot(x, Ox, 'k')
plt.legend()
plt.title("Aproximación de f con el polinomio de McLaurin")
plt.show()
