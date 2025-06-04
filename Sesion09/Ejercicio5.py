# -*- coding: utf-8 -*-
"""
Created on Apr 20, 2025
@author: UO299673
"""

import numpy as np
import sympy as sym

def montecarlo(f, a, b, n):
    # Paso 1: generar n puntos aleatorios en el intervalo [a,b]
    x_rand = np.random.rand(n) * (b - a) + a
    y_rand = f(x_rand)

    # Paso 2: estimamos el valor de la integral como la media de las alturas
    integral_aprox = np.mean(y_rand) * (b - a)

    return integral_aprox

# ---- Prueba con la función 10 e^{-x^2} - 6 entre [-2,2]
f = lambda x: 10 * np.exp(-x**2) - 6
a, b = -2, 2
n = 100000  # puedes aumentar esto para más precisión

aprox = montecarlo(f, a, b, n)

# Valor exacto simbólico
x = sym.Symbol('x')
I_exacta = sym.integrate(10 * sym.exp(-x**2) - 6, (x, a, b)).evalf()

print("El valor aproximado es", aprox)
print("El valor exacto es    ", I_exacta)
