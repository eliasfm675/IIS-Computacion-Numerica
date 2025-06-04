# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 23:11:29 2025

@author: Elías
"""

import numpy as np
import matplotlib.pyplot as plt
def sinh(x, grado):
    polinomio=0
    sumando=0
    factorial=1
    for i in range(1, grado+1, 2):
        if np.abs(sumando-(x**i)/factorial)<1e-5:
            break
        sumando=(x**i)/factorial
        polinomio+=sumando
        factorial*=i+2
     
    return polinomio
def cosh(x, grado):
    polinomio=0
    sumando=0
    factorial=1
    for i in range(0, grado+1, 2):
        if np.abs(sumando-(x**i)/factorial)<1e-5:
            break
        sumando=(x**i)/factorial
        polinomio+=sumando
        factorial*=i+2

    return polinomio
def tanh(x, grado):
    return sinh(x, grado)/cosh(x,grado)
x=0.5
grado=7
print("Valor aprox = " + str(tanh(x, grado)))
print("Valor exacto = " + str(np.tanh(x)))