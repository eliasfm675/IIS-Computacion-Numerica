# -*- coding: utf-8 -*-
"""
Created on Mon Mar 24 13:05:32 2025

@author: Elías
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as op

f = lambda x: x**3 -75
a=0
b=5
x=np.linspace(a, b)
raiz = op.bisect(f, a, b, xtol=10**-7, maxiter=100)
print("%.6f"%raiz)
plt.figure()
plt.plot(x, 0*x, 'k')
plt.plot(x, f(x))
plt.plot(raiz, 0, 'ro')