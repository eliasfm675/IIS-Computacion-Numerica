import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d, CubicSpline

# Función original
f = lambda x: np.cos(x)

# Nodos
x = np.arange(0, 11)          # x = [0, 1, ..., 10]
y = f(x)                      # y = cos(x)

# Puntos de evaluación
xp = np.linspace(0, 10, 100)
yp_true = f(xp)

# Interpolación lineal a trozos
f_lineal = interp1d(x, y, kind='linear')
yp_lineal = f_lineal(xp)

# Interpolación con splines cúbicos naturales
f_spline = CubicSpline(x, y, bc_type='natural')
yp_spline = f_spline(xp)

# Cálculo de errores
Ea_lineal = np.linalg.norm(yp_lineal - yp_true)
Ea_spline = np.linalg.norm(yp_spline - yp_true)

print(f"Error interpolación lineal a trozos = {Ea_lineal:.5f}")
print(f"Error interpolación con splines     = {Ea_spline:.5f}")

# Graficar interpolaciones
plt.figure()
plt.plot(x, y, 'ro', label='Nodos')
plt.plot(xp, yp_true, 'k--', label='cos(x)')
plt.plot(xp, yp_lineal, 'b-', label='Lineal a trozos')
plt.title("Interpolación lineal a trozos")
plt.legend()
plt.grid(True)
plt.show()

plt.figure()
plt.plot(x, y, 'ro', label='Nodos')
plt.plot(xp, yp_true, 'k--', label='cos(x)')
plt.plot(xp, yp_spline, 'g-', label='Spline cúbico')
plt.title("Interpolación con spline cúbico")
plt.legend()
plt.grid(True)
plt.show()
