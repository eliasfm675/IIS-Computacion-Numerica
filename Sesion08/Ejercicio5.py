import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

def fourier_series(f, T, n_terms, a, b, n_points=500):
    """
    Calcula y dibuja la serie de Fourier de una función
    
    Parámetros:
    f: función a aproximar
    T: periodo de la función
    n_terms: número de términos de la serie
    a, b: intervalo para graficar
    n_points: número de puntos para la gráfica
    """
    
    # Coeficiente a0
    def integrand_a0(x):
        return f(x)
    a0 = (2/T) * quad(integrand_a0, 0, T)[0]
    
    # Coeficientes an y bn
    coefficients = {'a': [a0/2], 'b': [0]}  # b0 no existe (sería 0)
    
    for n in range(1, n_terms+1):
        # Coeficiente an
        def integrand_an(x):
            return f(x) * np.cos(2*n*np.pi*x/T)
        an = (2/T) * quad(integrand_an, 0, T)[0]
        coefficients['a'].append(an)
        
        # Coeficiente bn
        def integrand_bn(x):
            return f(x) * np.sin(2*n*np.pi*x/T)
        bn = (2/T) * quad(integrand_bn, 0, T)[0]
        coefficients['b'].append(bn)
    
    # Función de la serie de Fourier
    def fourier_func(x):
        result = coefficients['a'][0]
        for n in range(1, n_terms+1):
            result += coefficients['a'][n] * np.cos(2*n*np.pi*x/T)
            result += coefficients['b'][n] * np.sin(2*n*np.pi*x/T)
        return result
    
    # Graficar
    x = np.linspace(a, b, n_points)
    y_original = f(x)
    y_fourier = fourier_func(x)
    
    plt.figure(figsize=(10, 6))
    plt.plot(x, y_original, 'b-', label='Función original')
    plt.plot(x, y_fourier, 'r--', label=f'Serie Fourier (n={n_terms})')
    plt.title(f'Aproximación con serie de Fourier (T={T}, {n_terms} términos)')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    plt.show()
    
    return coefficients

# Ejemplo 1: f(x) = x en [0,3] con T=3 y 5 términos
print("\n--- Serie de Fourier para f(x) = x en [0,3] (T=3) con 5 términos ---")
f1 = lambda x: x
coeff1 = fourier_series(f1, T=3, n_terms=5, a=0, b=3)

# Ejemplo 2: f(x) = (x-pi)^2 en [0,2pi] con T=2pi y 6 términos
print("\n--- Serie de Fourier para f(x) = (x-pi)^2 en [0,2pi] (T=2pi) con 6 términos ---")
f2 = lambda x: (x-np.pi)**2
coeff2 = fourier_series(f2, T=2*np.pi, n_terms=6, a=0, b=2*np.pi)