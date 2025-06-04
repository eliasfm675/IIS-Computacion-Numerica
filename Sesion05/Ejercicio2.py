import numpy as np
import matplotlib.pyplot as plt

np.set_printoptions(precision=5, suppress=True)

# Función de bisección
def bisection(f, a, b, tol=1.e-6, maxiter=100):
    error = np.inf
    k = 0
    x = a
    while error > tol and k < maxiter:
        xant = x
        x = (a + b) / 2
        if f(a) * f(x) < 0:
            b = x
        elif f(b) * f(x) < 0:
            a = x
        else:
            return x, k + 1
        error = np.abs(x - xant)
        k += 1
    return x, k

# Funciones dadas
f1 = lambda x: x**5 - 3 * x**2 + 1.6
f2 = lambda x: ((x**3 + 1) / (x**2 + 1)) * np.cos(x) - 0.2

# Función para encontrar todas las raíces en un intervalo
def find_roots(f, a, b, N=100):
    x = np.linspace(a, b, N)  # Dividir el intervalo en N puntos
    roots = []
    
    for i in range(len(x) - 1):
        if f(x[i]) * f(x[i+1]) < 0:  # Cambio de signo => hay raíz
            root, _ = bisection(f, x[i], x[i+1])
            roots.append(root)
    
    return np.array(roots)

# Encontrar raíces de f1 en [-3, 3] y de f2 en [-3, 3]
roots_f1 = find_roots(f1, -3, 3, 200)
roots_f2 = find_roots(f2, -3, 3, 200)

print("Raíces de f1:", np.round(roots_f1, 5))
print("Raíces de f2:", np.round(roots_f2, 5))

# Graficar f1 con sus raíces
x = np.linspace(-3, 3, 500)
plt.figure()
plt.plot(x, f1(x), label='f1(x)')
plt.axhline(0, color='black', linestyle='--')
plt.scatter(roots_f1, np.zeros_like(roots_f1), color='red', label='Raíces', zorder=3)
plt.ylim(-5, 5)
plt.grid(True)
plt.legend()
plt.title('Raíces de f1(x)')
plt.show()

# Graficar f2 con sus raíces
plt.figure()
plt.plot(x, f2(x), label='f2(x)')
plt.axhline(0, color='black', linestyle='--')
plt.scatter(roots_f2, np.zeros_like(roots_f2), color='red', label='Raíces', zorder=3)
plt.ylim(-2, 2)
plt.grid(True)
plt.legend()
plt.title('Raíces de f2(x)')
plt.show()
