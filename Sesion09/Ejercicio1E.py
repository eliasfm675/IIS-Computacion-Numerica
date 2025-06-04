# -*- coding: utf-8 -*-
"""
Created on Mar 31, 2025
@author: UO299673
"""

import numpy as np
import matplotlib.pyplot as plt
import sympy as sym

# Dibujo del área
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
    plt.plot([a, a, b, b], [f(a), 0, 0, f(b)], 'b')
    plt.plot(nodos, f(nodos), 'ro', label='Puntos de interpolación')
    plt.plot(xp, yp, 'r--', label='Área aproximada (trapecio)')
    plt.plot([a, a, b, b], [pa, 0, 0, pb], 'r--')
    plt.legend()
    plt.title("Aproximación por Regla del Trapecio Compuesta")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid()
    plt.show()

# Regla del Trapecio compuesta
def trapecio_comp(f, a, b, n):
    h = (b - a) / n
    suma = 0.5 * (f(a) + f(b))  # extremos con peso 1/2
    for i in range(1, n):
        xi = a + i * h
        suma += f(xi)
    I = h * suma
    return I

# Parámetros
f = lambda x: np.log(x)
a = 1
b = 3
n = 4

# Puntos de los nodos (extremos de subintervalos)
nodos = np.linspace(a, b, n + 1)

# Aproximación
I_aprox = trapecio_comp(f, a, b, n)

# Valor exacto con sympy
x = sym.Symbol('x', real=True)
f_sym = sym.log(x)
I_exacta = sym.integrate(f_sym, (x, a, b))

# Mostrar resultados
print("El valor aproximado es", I_aprox)
print("El valor exacto es    ", float(I_exacta))

# Dibujo
dibujo(f, a, b, nodos)
