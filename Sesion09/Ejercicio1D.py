# -*- coding: utf-8 -*-
"""
Created on Mon Mar 31 15:31:33 2025
@author: UO299673
"""

import numpy as np
import matplotlib.pyplot as plt
import sympy as sym

# Función de dibujo del área y de la interpolación
def dibujo(f, a, b, nodos):
    x = np.linspace(a, b, 100)
    p = np.polyfit(nodos, f(nodos), len(nodos) - 1)
    xp = np.linspace(a, b)
    yp = np.polyval(p, xp)
    pa = np.polyval(p, a)
    pb = np.polyval(p, b)

    plt.figure()
    plt.plot(x, 0 * x, 'k')
    plt.plot(x, f(x), label='Área exacta')
    plt.plot([a, a, b, b], [f(a), 0, 0, f(b)], 'b')
    plt.plot(nodos, f(nodos), 'ro', label='Puntos de interpolación')
    plt.plot(xp, yp, 'r--', label='Área aproximada')
    plt.plot([a, a, b, b], [pa, 0, 0, pb], 'r--')
    plt.legend()
    plt.title("Aproximación por Punto Medio")
    plt.grid(True)
    plt.show()

# Implementación de la regla del punto medio compuesta
def punto_medio_comp(f, a, b, n):
    h = (b - a) / n
    suma = 0
    for i in range(n):
        xi = a + i * h
        xm = xi + h / 2  # Punto medio del subintervalo
        suma += f(xm)
    I = h * suma
    return I

# Parámetros del problema
f = lambda x: np.log(x)
a = 1
b = 3
n = 5

# Cálculo aproximado
I_aprox = punto_medio_comp(f, a, b, n)

# Cálculo exacto con sympy
x = sym.Symbol('x', real=True)
f_sim = sym.log(x)
I_exacta = sym.integrate(f_sim, (x, a, b))

# Mostrar resultados
i = (a + b) / 2
nodos = np.array([i])
dibujo(f, a, b, nodos)

print("El valor aproximado es ", I_aprox)
print("El valor exacto es     ", float(I_exacta))
