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
        sumando=(x**i)/factorial
        if operacion:
            polinomio+=sumando
            operacion=False
        else:
            polinomio-=sumando
            operacion=True
        factorial*=i+2
        i+=2
    print("Valor aprox = "+ str(polinomio))
    print("Valor exacto = "+ str(f(x)))
    print("Número de iteraciones = "+ str(i))
McL(x0,tol,maxNumSum)
