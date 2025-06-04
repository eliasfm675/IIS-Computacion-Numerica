# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 12:48:02 2025

@author: Elías
"""

import numpy as np
import matplotlib.pyplot as plt
PI = np.pi
def f(x):
    y = np.piecewise(x, 
                     [(-PI < x) & (x < 0), (x == 0) | (x == -PI) | (x == PI), (0 < x) & (x < PI)],
                     [-1, 0, 1])
    
    # Compute Fourier series approximation
    serie = np.zeros_like(x, dtype=np.float64)
    for n in range(1,101):
        serie+= (1/(2*n-1))*(np.sin((2*n-1)*x))
    return (4/PI)*serie
x=np.linspace(-PI, PI, 500)
Ox=0*x
plt.figure()
plt.plot(x, f(x))
plt.plot(x,Ox)
plt.show()


    