# -*- coding: utf-8 -*-
"""
Created on Mon Mar 24 12:51:40 2025

@author: Elías
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as op
f = lambda x: np.cosh(x)*np.cos(x)-1
x0=np.linspace(0, 5, 100)
raiz = op.newton(f, x0, tol=10**-7, maxiter=100)
print("%.6f"%raiz[-1])
plt.figure()
plt.plot(x0, f(x0))
plt.plot(x0, 0*x0, 'k')
plt.plot(raiz[-1], 0, 'ro')
plt.show()