# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 15:30:09 2025

@author: uo299673
"""


import numpy as np
import matplotlib.pyplot as plt
import numpy.polynomial.polynomial as pol
import time

def HornerV(x, p):
    y=np.zeros_like(x)
    n = len(p)
    q = np.zeros(n)
    q[-1] = p[-1]
    for j in range(len(x)):
        for i in range(n-2, -1, -1):
            q[i]=q[i+1]*x[j]+p[i]
            y[j]=q[i]
    cociente = q[1:]
    resto = q[0]
    return y
def hornerVect(x, p):
    y = np.zeros_like(x)
    n = len(p)
    q = np.zeros(n)
    y = p[n-1]
    for i in range(n-2, -1, -1):
        y = y* x+ p[i]
    return y



p = np.array([1., -1, 2, -3, 5, -2])
x = np.linspace(-1, 1, 1000000)
r = np.array([1., -1, -1, 1, -1, 0, -1, 1])

t=time.time()

plt.figure()
plt.plot(x, HornerV(x, r))
plt.plot(x, 0*x, 'k')
plt.title('Polinomio R')

plt.figure()
plt.plot(x, HornerV(x, p))
plt.plot(x, 0*x, 'k')
plt.title('Polinomio P')

t1=time.time()
tf1=t1-t
print("Tiempo sin vectorización --> ", tf1)
t=time.time()
plt.figure()
plt.plot(x, hornerVect(x, p))
plt.plot(x, 0*x, 'k')
plt.title('Polinomio P(HornerV)')


plt.figure()
plt.plot(x, hornerVect(x, r))
plt.plot(x, 0*x, 'k')
plt.title('Polinomio R(HornerV)')

t1=time.time()
tf2=t1-t
print("Tiempo con vectorización --> ", tf2)
