# -*- coding: utf-8 -*-
"""
Created on Mon Mar 10 16:02:43 2025

@author: UO299673
"""
import numpy as np
import matplotlib.pyplot as plt
import sympy as sym
import scipy.optimize as op




x=sym.Symbol('x', real=True)
f_sim =  x**2 + sym.log(2*x+7)*sym.cos(3*x)+0.1
df_sim= sym.diff(f_sim, x)
d2f_sim=sym.diff(df_sim, x)
f= sym.lambdify([x], f_sim,'numpy')
df= sym.lambdify([x], df_sim, 'numpy')
d2f = sym.lambdify([x], d2f_sim, 'numpy')





x=np.linspace(-1.0, 3.0, 5)
roots = op.newton(df,x, tol=10**-6, maxiter=100)
print(roots)
x=np.linspace(-1.0, 3.0,200)

maxRoots=roots[1::2]
print(maxRoots)
minRoots=roots[::2]
print(minRoots)

plt.figure()
plt.plot(x, df(x))
plt.plot(x, 0*x, 'k')
plt.title("Función derivada de f")
plt.show()

x=np.linspace(-2.0, 4.0, 200)

plt.figure()
plt.plot(x, f(x))
plt.plot(x, 0*x, 'k')
plt.plot(maxRoots, f(maxRoots), 'ro')
plt.plot(minRoots, f(minRoots), 'go')
plt.show()


x=np.linspace(-1.0, 4.0, 200)
plt.figure()
plt.plot(x, d2f(x))
plt.title("Función derivada segunda de f")
plt.plot(x, x*0, 'k')
plt.show()

x=np.linspace(-1.0, 4.0,200)
inflection= op.newton(d2f, x, tol=1.e-6, maxiter=100)
print(inflection)

plt.figure()
plt.plot(x, f(x), label="Función f")
plt.plot(x, x*0, 'k')
plt.plot(inflection, f(inflection), 'bo', label="Puntos de inflexión")
plt.xlim(-1.5, 4.5)
plt.ylim(-1.5, 19.5)
plt.show()