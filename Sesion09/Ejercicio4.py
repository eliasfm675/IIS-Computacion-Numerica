# -*- coding: utf-8 -*-
"""
Created on Apr 20, 2025
@author: UO299673
"""

import numpy as np
import sympy as sym

def montecarlo(f, a, b, n):
    # Paso 1: estimamos el valor máximo de f(x) en [a, b]
    x = np.linspace(a, b, 1000)
    fmax = np.max(f(x))

    # Paso 2: generamos n puntos aleatorios en el rectángulo [a,b] x [0,fmax]
    x_rand = np.random.rand(n) * (b - a) + a
    y_rand = np.random.rand(n) * fmax

    # Paso 3: contamos cuántos puntos caen por debajo de la curva
    debajo = y_rand < f(x_rand)

    # Paso 4: proporción * área del rectángulo
    area_rect = (b - a) * fmax
    integral_aprox = area_rect * np.mean(debajo)

    return integral_aprox

# ---- Prueba con la función e^{-x^2} entre [-2,2]
f = lambda x: np.exp(-x**2)
a, b = -2, 2
n = 100000  # puedes aumentar esto para más precisión

aprox = montecarlo(f, a, b, n)

# Valor exacto simbólico
x = sym.Symbol('x')
I_exacta = sym.integrate(sym.exp(-x**2), (x, a, b)).evalf()

print("El valor aproximado es", aprox)
print("El valor exacto es    ", I_exacta)
