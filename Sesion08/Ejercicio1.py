# -*- coding: utf-8 -*-
"""
Created on Mon Mar 24 15:56:34 2025

@author: UO299673
"""

import numpy as np
import matplotlib.pyplot as plt
import numpy.polynomial.polynomial as pol

np.set_printoptions(precision=2)  # solo dos decimales
np.set_printoptions(suppress=True)  # no usar notación exponencial

def aprox1(f, g, a, b, n):
    # 1. Construir los nodos x y obtener y = f(x)
    x_nodes = np.linspace(a, b, n)
    y_nodes = f(x_nodes)
    
    # 2. Construir la matriz V del sistema (1)
    V = np.zeros((n, g+1))
    for i in range(n):
        for j in range(g+1):
            V[i, j] = x_nodes[i]**j
    
    # 3. Construir C y d del sistema (2)
    C = np.dot(V.T, V)
    d = np.dot(V.T, y_nodes)
    
    # 4. Resolver el sistema Cp = d
    p = np.linalg.solve(C, d)
    
    # Imprimir resultados
    print("\nMatriz del sistema C:")
    print(C)
    print("\nTérmino independiente d:")
    print(d)
    print("\nSolución del sistema p (coeficientes del polinomio):")
    print(p)
    
    # 5. Obtener puntos para dibujar el polinomio
    x_plot = np.linspace(a, b, 50)
    y_plot = pol.polyval(x_plot, p)
    
    # 6. Dibujar
    plt.figure()
    plt.plot(x_nodes, y_nodes, 'ro', label='Puntos originales')  # puntos originales
    plt.plot(x_plot, y_plot, 'b-', label=f'Polinomio grado {g}')  # polinomio
    plt.plot(x_plot, f(x_plot), 'g--', label='Función original')  # función original
    plt.legend()
    plt.title(f'Aproximación polinómica de grado {g} con {n} puntos')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.show()

# Ejemplo 1: sin(x) con grado 2 y 5 puntos
print("\n--- Ejemplo 1: f(x) = sin(x), grado 2, 5 puntos en [0, 2] ---")
a, b = 0, 2
n = 5
g = 2
f1 = lambda x: np.sin(x)
aprox1(f1, g, a, b, n)

# Ejemplo 2: cos(arctan(x)) - log(x+5) con grado 4 y 10 puntos
print("\n--- Ejemplo 2: f(x) = cos(arctan(x)) - log10(x+5), grado 4, 10 puntos en [-2, 0] ---")
a, b = -2, 0
n = 10
g = 4
f2 = lambda x: np.cos(np.arctan(x)) - np.log10(x + 5)
aprox1(f2, g, a, b, n)