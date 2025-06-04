# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 15:30:09 2025

@author: uo299673
"""


import numpy as np
import matplotlib.pyplot as plt
import numpy.polynomial.polynomial as pol
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
p = np.array([1., -1, 2, -3, 5, -2])
x= np.linspace(-1,1)
r = np.array([1., -1, -1, 1, -1, 0, -1, 1])

plt.figure()
plt.plot(x, pol.polyval(x,r))
plt.plot(x,0*x,'k')
plt.title('Polinomio R')


plt.figure()
plt.plot(x, pol.polyval(x,p))
plt.plot(x,0*x,'k')
plt.title('Polinomio P')

plt.figure()
plt.plot(x, HornerV(x,p))
plt.plot(x,0*x,'k')
plt.title('Polinomio P(HornerV)')


plt.figure()
plt.plot(x, HornerV(x,r))
plt.plot(x,0*x,'k')
plt.title('Polinomio R(HornerV)')