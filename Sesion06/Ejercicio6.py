# -*- coding: utf-8 -*-
"""
Created on Mon Mar 24 13:09:28 2025

@author: Elías
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as op
import sympy as sym
x=sym.Symbol('x', real=True)
f_sim=sym.exp(-x**2)*sym.log(x**2 +1)
df_sim=sym.diff(f_sim,x)
d2f_sim=sym.diff(df_sim,x)
f=sym.lambdify([x], f_sim, 'numpy')
df=sym.lambdify([x], df_sim, 'numpy')
d2f=sym.lambdify([x],d2f_sim,'numpy')
x0=np.linspace(-2, 2,100)
x1=np.linspace(-1, 1,3)
pts=op.fsolve(df, x1)
pts2=op.fsolve(d2f,x1)
print('Extremos')
print(pts)
print(pts2)
plt.figure()
plt.plot(x0,0*x0,'k')
plt.plot(x0,f(x0))
plt.plot(pts,pts, 'ro')
plt.ylim(-1,1)
plt.xlim(-2,2)
plt.show()