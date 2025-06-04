import numpy as np
import matplotlib.pyplot as plt

def dif_div(x, y):
    n = len(x)
    tabla = np.zeros((n, n))
    tabla[:, 0] = y

    for j in range(1, n):
        for i in range(n - j):
            tabla[i, j] = (tabla[i+1, j-1] - tabla[i, j-1]) / (x[i+j] - x[i])
    
    # Mostrar tabla como en el ejemplo
    tabla_completa = np.zeros((n, n+1))
    tabla_completa[:, 0] = x
    tabla_completa[:, 1:] = tabla
    print("TABLA DE DIFERENCIAS DIVIDIDAS")
    print(np.round(tabla_completa, 4))
    return tabla[0]  # Coeficientes del polinomio

def polinomio_newton(x, y, z):
    coef = dif_div(x, y)
    n = len(x)
    if np.isscalar(z):
        z = np.array([z])
    p = np.zeros_like(z, dtype=float)

    for i in range(len(z)):
        pz = coef[0]
        mult = 1.0
        for j in range(1, n):
            mult *= (z[i] - x[j-1])
            pz += coef[j] * mult
        p[i] = pz
    return p

# NODOS de prueba
x = np.array([-1., 0, 2, 3, 5])
y = np.array([ 1., 3, 4, 3, 1])

# Evaluación y gráfica
z = np.linspace(min(x), max(x), 500)
pz = polinomio_newton(x, y, z)

plt.plot(x, y, 'ro', label='Nodos')
plt.plot(z, pz, 'b-', label='Polinomio interpolante')
plt.title("Interpolación de Newton con diferencias divididas")
plt.legend()
plt.grid(True)
plt.show()

# Comprobación con nuevos nodos
x1 = np.array([-1., 0, 2, 3, 5, 6, 7])
y1 = np.array([ 1., 3, 4, 3, 2, 2, 1])

z1 = np.linspace(min(x1), max(x1), 500)
pz1 = polinomio_newton(x1, y1, z1)

plt.plot(x1, y1, 'go', label='Nodos nuevos')
plt.plot(z1, pz1, 'm-', label='Polinomio interpolante (nuevos nodos)')
plt.title("Interpolación con nuevos nodos")
plt.legend()
plt.grid(True)
plt.show()
