# -*- coding: utf-8 -*-
"""
Created on Apr 20, 2025
@author: UO299673
"""

import numpy as np
import sympy as sym

def gauss(f, a, b, n):
    # Obtener nodos y pesos de Gauss-Legendre en [-1, 1]
    x, w = np.polynomial.legendre.leggauss(n)

    # Transformar nodos al intervalo [a, b]
    y = 0.5 * (b - a) * x + 0.5 * (a + b)
    w_trans = 0.5 * (b - a) * w

    # Evaluar la fórmula de cuadratura
    integral = np.sum(w_trans * f(y))
    return integral

# Definir la función y los límites
f = lambda x: np.log(x)
a = 1
b = 3

# Cálculo exacto con sympy
x = sym.Symbol('x', real=True)
f_sym = sym.log(x)
I_exacta = sym.integrate(f_sym, (x, a, b))
I_exacta_float = float(I_exacta)

# Probar con n = 1, 2 y 3
for n in [1, 2, 3]:
    I_aprox = gauss(f, a, b, n)
    print(f"\nn = {n}")
    print("El valor aproximado es", I_aprox)
    print("El valor exacto es    ", I_exacta_float)
