import numpy as np
import numpy.polynomial.polynomial as pol
import matplotlib.pyplot as plt
import pandas as pd

# Cargar los datos
df = pd.read_csv('http://www.unioviedo.es/compnum/laboratorios_py/new/cars.csv', sep=',')

# --------------------------
# Parte 1: Relación weight-horsepower
# --------------------------

# Extraer las variables weight y horsepower
x_weight = df['weight'].values
y_horsepower = df['horsepower'].values

# Calcular polinomio de grado 1 (regresión lineal)
p_horsepower = pol.polyfit(x_weight, y_horsepower, 1)

# Estimación para un coche de 3000 libras
weight_3000 = 3000
estimated_hp = pol.polyval(weight_3000, p_horsepower)
print(f"{estimated_hp:.0f} caballos")

# Crear puntos para la gráfica
x_plot = np.linspace(min(x_weight), max(x_weight), 100)
y_plot = pol.polyval(x_plot, p_horsepower)

# Dibujar
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plt.scatter(x_weight, y_horsepower, color='blue', label='Datos reales')
plt.plot(x_plot, y_plot, 'r-', label='Aproximación lineal')
plt.scatter([weight_3000], [estimated_hp], color='green', s=100, label=f'3000 lbs: {estimated_hp:.0f} HP')
plt.xlabel('Peso (lbs)')
plt.ylabel('Potencia (HP)')
plt.title('Relación Peso-Potencia')
plt.legend()
plt.grid(True)

# --------------------------
# Parte 2: Relación horsepower-mpg
# --------------------------

# Extraer las variables horsepower y mpg
x_horsepower = df['horsepower'].values
y_mpg = df['mpg'].values

# Calcular polinomio de grado 2
p_mpg = pol.polyfit(x_horsepower, y_mpg, 2)

# Estimación de mpg para la potencia calculada
estimated_mpg = pol.polyval(estimated_hp, p_mpg)
print(f"\n{estimated_mpg:.0f} mpg")

# Crear puntos para la gráfica
x_plot2 = np.linspace(min(x_horsepower), max(x_horsepower), 100)
y_plot2 = pol.polyval(x_plot2, p_mpg)

# Dibujar
plt.subplot(1, 2, 2)
plt.scatter(x_horsepower, y_mpg, color='blue', label='Datos reales')
plt.plot(x_plot2, y_plot2, 'r-', label='Aproximación cuadrática')
plt.scatter([estimated_hp], [estimated_mpg], color='green', s=100, label=f'{estimated_hp:.0f} HP: {estimated_mpg:.0f} mpg')
plt.xlabel('Potencia (HP)')
plt.ylabel('Millas por galón (MPG)')
plt.title('Relación Potencia-MPG')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()