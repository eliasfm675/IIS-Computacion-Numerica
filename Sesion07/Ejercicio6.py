import numpy as np
import matplotlib.pyplot as plt
import numpy.polynomial.polynomial as pol

# Función para construir la matriz de Vandermonde
def Vandermonde(x):
    n = len(x)
    V = np.vander(x, N=n, increasing=True)
    return V

# Función para resolver el sistema Vp = y y encontrar los coeficientes
def polVandermonde(x, y):
    V = Vandermonde(x)
    print('Matriz de Vandermonde V')
    print(np.round(V, 2))
    p = np.linalg.solve(V, y)
    print('Coeficientes del polinomio')
    print(np.round(p, 4))
    return p

# Función para graficar
def dibujar_pol(x, y, p):
    xp = np.linspace(min(x), max(x), 100)
    yp = pol.polyval(xp, p)

    plt.plot(x, y, 'ro', label='Nodos')
    plt.plot(xp, yp, 'b-', label='Pol. interpolante')
    plt.title("Interpolación con matriz de Vandermonde")
    plt.grid(True)
    plt.legend()
    plt.show()

# ---- Prueba con los primeros nodos ----
x = np.array([-1., 0, 2, 3, 5])
y = np.array([ 1., 3, 4, 3, 1])
p = polVandermonde(x, y)
dibujar_pol(x, y, p)

# ---- Prueba con nuevos nodos ----
x1 = np.array([-1., 0, 2, 3, 5, 6, 7])
y1 = np.array([ 1., 3, 4, 3, 2, 2, 1])
p1 = polVandermonde(x1, y1)
dibujar_pol(x1, y1, p1)

# Comparación con polyvander (no recomendado por estabilidad)
print("Matriz de Vandermonde usando polyvander:")
va = pol.polyvander(x, len(x)-1)
print(np.round(va, 2))
