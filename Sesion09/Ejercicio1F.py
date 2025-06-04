# -*- coding: utf-8 -*-
"""
Created on Mar 31, 2025
@author: UO299673
"""

import numpy as np
import matplotlib.pyplot as plt
import sympy as sym

# Dibujo del área aproximada
def dibujo(f, a, b, nodos):
    x = np.linspace(a, b, 100)
    p = np.polyfit(nodos, f(nodos), len(nodos) - 1)
    xp = np.linspace(a, b)
    yp = np.polyval(p, xp)
    pa = np.polyval(p, a)
    pb = np.polyval(p, b)

    plt.figure()
    plt.plot(x, 0 * x, 'k')
    plt.plot(x, f(x), label='Área exacta (f)')
    plt.plot(nodos, f(nodos), 'ro', label='Puntos de interpolación')
    plt.plot(xp, yp, 'r--', label='Área aproximada (Simpson)')
    plt.legend()
    plt.title("Aproximación por Regla de Simpson Compuesta")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid()
    plt.show()

# Regla de Simpson compuesta
def simpson_comp(f, a, b, n):
    if n % 2 != 0:
        raise ValueError("Simpson requiere un número PAR de subintervalos.")
    
    h = (b - a) / n
    suma = f(a) + f(b)

    for i in range(1, n, 2):
        xi = a + i * h
        suma += 4 * f(xi)
    
    for i in range(2, n-1, 2):
        xi = a + i * h
        suma += 2 * f(xi)

    return h * suma / 3

# Parámetros
f = lambda x: np.log(x)
a = 1
b = 3
n = 4  # Debe ser par

# Nodos para dibujo (x_0, x_1, ..., x_n)
nodos = np.linspace(a, b, n + 1)

# Aproximación
I_aprox = simpson_comp(f, a, b, n)

# Valor exacto con sympy
x = sym.Symbol('x', real=True)
f_sym = sym.log(x)
I_exacta = sym.integrate(f_sym, (x, a, b))

# Mostrar resultados
print("El valor aproximado es", I_aprox)
print("El valor exacto es    ", float(I_exacta))

# Dibujo
dibujo(f, a, b, nodos)
