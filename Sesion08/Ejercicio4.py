import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
from scipy.special import eval_legendre

def aprox3(f, g_degree, a, b):
    """
    Calcula y dibuja el polinomio de aproximación usando polinomios de Legendre
    
    Parámetros:
    f: función a aproximar
    g_degree: grado del polinomio de aproximación
    a, b: límites del intervalo
    """
    
    # Función para transformar el intervalo [a,b] a [-1,1]
    def transform(t):
        return (2*t - (a + b)) / (b - a)
    
    # Calcular coeficientes a_k
    coefficients = []
    for k in range(g_degree + 1):
        # Numerador: integral de L_k(x)*f(x) dx
        integrand_num = lambda t: eval_legendre(k, transform(t)) * f(t)
        num = quad(integrand_num, a, b)[0]
        
        # Denominador: integral de L_k(x)^2 dx
        integrand_den = lambda t: eval_legendre(k, transform(t))**2
        den = quad(integrand_den, a, b)[0]
        
        a_k = num / den
        coefficients.append(a_k)
        
        # Imprimir resultados parciales
        print(f"\na{k} num = {num}")
        print(f"a{k} den = {den}")
        print(f"a{k}     = {a_k}")
    
    # Crear función del polinomio aproximado
    def legendre_poly(x):
        result = 0
        for k in range(g_degree + 1):
            result += coefficients[k] * eval_legendre(k, transform(x))
        return result
    
    # Evaluar y graficar
    x_plot = np.linspace(a, b, 100)
    y_f = f(x_plot)
    y_p = legendre_poly(x_plot)
    
    plt.figure()
    plt.plot(x_plot, y_f, 'b-', label='Función original')
    plt.plot(x_plot, y_p, 'r--', label=f'Aprox. Legendre grado {g_degree}')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(f'Aproximación con polinomios de Legendre (grado {g_degree})')
    plt.legend()
    plt.grid(True)
    plt.show()

# Ejemplo 1: cos(x) con grado 2 en [0, 2]
print("\n--- Aproximación de cos(x) con polinomios de Legendre de grado 2 en [0, 2] ---")
f1 = lambda x: np.cos(x)
aprox3(f1, 2, 0, 2)

# Ejemplo 2: cos(arctan(x)) - log(x+5) con grado 4 en [-2, 0]
print("\n--- Aproximación de cos(arctan(x)) - log10(x+5) con polinomios de Legendre de grado 4 en [-2, 0] ---")
f2 = lambda x: np.cos(np.arctan(x)) - np.log10(x + 5)
aprox3(f2, 4, -2, 0)