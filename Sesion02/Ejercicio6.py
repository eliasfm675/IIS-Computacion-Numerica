# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 23:11:29 2025

@author: Elías
"""

import numpy as np
import matplotlib.pyplot as plt
def sinh(x, tol):
    polinomio=0
    sumando=0
    factorial=1
    grado=100
    for i in range(1, grado+1,2):
        if np.all(np.abs((sumando - (x**i)) / factorial) < tol):
            break
        sumando=(x**i)/factorial
        polinomio+=sumando
        factorial*=i+2
    return polinomio
def cosh(x, tol):
    polinomio=0
    sumando=0
    factorial=1
    grado=100
    for i in range(0,grado+1,2):
        if np.all(np.abs((sumando - (x**i)) / factorial) < tol):
            break
        sumando=(x**i)/factorial
        polinomio+=sumando
        factorial*=i+2
        i+=2
    return polinomio
def funTanh(x, tol):
    return sinh(x, tol)/cosh(x,tol)
f= lambda x: np.tanh(x)
x=np.linspace(-3, 3, 50)
Ox=0*x
grado=8
tol=1e-8
plt.figure()
plt.plot(x,f(x), label="f")
plt.plot(x, funTanh(x, tol), label="Aproximación de f")
plt.plot(x, Ox, 'k')
plt.title("Aproximación de f con el polinomio de McLaurin")
plt.legend()
plt.show()
