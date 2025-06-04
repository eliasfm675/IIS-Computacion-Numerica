# -*- coding: utf-8 -*-
"""
Created on Apr 20, 2025
@author: UO299673
"""

import numpy as np
import sympy as sym

# Regla del punto medio (compuesta para n=1)
def punto_medio(f, a, b):
    m = (a + b) / 2
    return (b - a) * f(m)

# Regla del trapecio
def trapecio(f, a, b):
    return (b - a) * (f(a) + f(b)) / 2

# Regla de Simpson
def simpson(f, a, b):
    m = (a + b) / 2
    return (b - a) * (f(a) + 4 * f(m) + f(b)) / 6

# Newton-Cotes general
def newton_cotes(f, a, b, n):
    if n == 1:
        return punto_medio(f, a, b)
    elif n == 2:
        return trapecio(f, a, b)
    elif n == 3:
        return simpson(f, a, b)
    else:
        raise ValueError("Newton-Cotes solo implementado para n = 1, 2, 3")

# Cuadratura de Gauss
def gauss(f, a, b, n):
    x, w = np.polynomial.legendre.leggauss(n)
    y = 0.5 * (b - a) * x + 0.5 * (a + b)
    w_trans = 0.5 * (b - a) * w
    return np.sum(w_trans * f(y))

# Determina el grado de precisión
def grado_de_precision(formula, n, a=1, b=3):
    x = sym.Symbol('x')
    precision = 0
    tolerancia = 1e-10

    while True:
        f_sym = x ** precision
        f_lamb = sym.lambdify(x, f_sym, "numpy")
        I_exacta = sym.integrate(f_sym, (x, a, b))
        try:
            I_aprox = formula(f_lamb, a, b, n)
        except Exception as e:
            print("Error al calcular la fórmula:", e)
            break

        error = abs(float(I_exacta - I_aprox))
        print(f"f(x) = x^{precision}   error = ", error)

        if error > tolerancia:
            break
        precision += 1

    print("\nEl grado de precisión es", precision - 1, "\n")


# --------- Ejecutar pruebas -----------

print("----  Fórmula del punto medio (n = 1) ----\n")
grado_de_precision(newton_cotes, 1)

print("----  Fórmula del trapecio (n = 2) ----\n")
grado_de_precision(newton_cotes, 2)

print("----  Fórmula de Simpson (n = 3) ----\n")
grado_de_precision(newton_cotes, 3)

for n in [1, 2, 3, 4]:
    print(f"----  Fórmula Gauss n = {n}  ----\n")
    grado_de_precision(gauss, n)
