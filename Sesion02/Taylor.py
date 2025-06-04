# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 15:58:08 2025

@author: UO299673
"""

import numpy as np
import matplotlib.pyplot as plt
import time
f = lambda x: np.exp(x)
def P(x0, grado):
    polinomio=0
    sumando=0
    factorial=1
    for i in range(grado+1):
        sumando=(x0**i)/factorial
        polinomio+=sumando
        factorial*=i+1
    return polinomio
a=-1;b=1
x=np.linspace(a, b,5)
Ox=0*x
plt.figure()
plt.plot(x,f(x), label="f")
plt.plot(x,Ox)
plt.plot(x,P(x,2), label="Taylor 2")