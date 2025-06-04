# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 15:46:00 2025

@author: UO299673
"""
import numpy as np
import matplotlib.pyplot as plt
import sympy as sym
def newton(f,df,x0,tol=1.e-6, maxiter=100):
    error=np.inf
    k=0
    x=x0
    xant=0
    while error>tol and k<maxiter:
        xant=x
        x=xant-(f(x))/df(x)
        error=np.abs(x-xant)
        k+=1
    return x, k
def find_roots(f,df, a, b, N=100):
    x_vals = np.linspace(a, b, N)  # Dividir el intervalo en N puntos
    roots = []
    
    for i in range(len(x_vals) - 1):
        if f(x_vals[i]) * f(x_vals[i+1]) < 0:  # Cambio de signo => hay raíz
            root, _ = newton(f, df, x_vals[i])
            if root not in roots:
                roots.append(root)
    
    return np.array(roots)
x=sym.Symbol('x', real=True)
f1_sim=x**5 - 3 * x**2 + 1.6 
df1_sim=sym.diff(f1_sim,x)

f2_sim=((x**3 + 1)/(x**2 + 1)*sym.cos(x))-0.2
df2_sim=sym.diff(f2_sim,x)

f1 = sym.lambdify([x], f1_sim, 'numpy')
f2=sym.lambdify([x], f2_sim, 'numpy')
df1=sym.lambdify([x], df1_sim, 'numpy')
df2=sym.lambdify([x], df2_sim, 'numpy')
x01=-1#lado izquierdo de los intervalos
x02=1
x03=-3
resultado, iteraciones = newton(f1, df1, x01)
print(resultado, iteraciones)
resultado, iteraciones = newton(f1, df1, x02)
print(resultado, iteraciones)
resultado, iteraciones = newton(f2, df2, x03)
print(resultado, iteraciones)
xp=np.array([-1,7567, -0.80596, 1.41334])
yp=np.array([0., 0., 0.])
roots_f1 = find_roots(f1, df1, -3, 3)
roots_f2 = find_roots(f2, df2, -3, 3)
x_plot = np.linspace(-3, 3, 500)
plt.figure()
plt.plot(x_plot, f1(x_plot), label='f1(x)')
plt.axhline(0, color='black', linestyle='--')
plt.scatter(roots_f1, np.zeros_like(roots_f1), color='red', label='Raíces', zorder=3)
plt.grid(True)
plt.legend()
plt.ylim(-2, 2)
plt.title('Raíces de f1(x)')
plt.show()

# Graficar f2 con sus raíces
plt.figure()
plt.plot(x_plot, f2(x_plot), label='f2(x)')
plt.axhline(0, color='black', linestyle='--')
plt.scatter(roots_f2, np.zeros_like(roots_f2), color='red', label='Raíces', zorder=3)
plt.grid(True)
plt.legend()
plt.title('Raíces de f2(x)')
plt.show()