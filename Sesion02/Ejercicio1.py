# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 16:09:05 2025

@author: UO299673
"""
import numpy as np
import matplotlib.pyplot as plt
f = lambda x: np.exp(x)
tol=1.e-8
x0=-0.4
def mcL(x0):
    polinomio=0
    sumando=1
    factorial=1
    i=0
    maxNumSum = 100
    while np.abs(sumando) > tol and i+1<=maxNumSum:
        sumando=(x0**i)/factorial
        polinomio+=sumando
        factorial*=i+1
        i+=1
    #return polinomio
    print("Valor de la aproximación en " + str(x0) + " = " + str(polinomio))
    print("Número de iteraciones = " + str(i))
        
print("Valor de la función en " + str(x0) + " = " + str(f(x0)))
print(mcL(x0))
      
