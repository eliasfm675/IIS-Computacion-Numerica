import numpy as np
import numpy.polynomial.polynomial as pol
import matplotlib.pyplot as plt
from scipy.integrate import quad

def aprox2(f, g_degree, a, b):
    """
    Calcula y dibuja el polinomio de aproximación de grado g_degree para la función f en [a,b]
    
    Parámetros:
    f: función a aproximar
    g_degree: grado del polinomio de aproximación
    a, b: límites del intervalo
    """
    
    # 1. Construir la matriz del sistema C
    C = np.zeros((g_degree+1, g_degree+1))
    for i in range(g_degree+1):
        for j in range(g_degree+1):
            # C[i,j] = integral de x^(i+j) dx desde a hasta b
            integrand = lambda x: x**(i+j)
            C[i,j] = quad(integrand, a, b)[0]
    
    # 2. Construir el vector de términos independientes d
    d = np.zeros(g_degree+1)
    for i in range(g_degree+1):
        # d[i] = integral de x^i * f(x) dx desde a hasta b
        integrand = lambda x: (x**i) * f(x)
        d[i] = quad(integrand, a, b)[0]
    
    # 3. Resolver el sistema Cp = d
    p = np.linalg.solve(C, d)
    
    # Imprimir resultados
    print("\nMatriz del sistema:")
    print(C)
    print("\nTérmino independiente:")
    print(d)
    print("\nCoeficientes del polinomio (de mayor a menor grado):")
    print(p[::-1])  # Invertimos para mostrar de mayor a menor grado
    
    # 4. Evaluar y graficar
    x_plot = np.linspace(a, b, 100)
    y_f = f(x_plot)
    y_p = pol.polyval(x_plot, p)
    
    plt.figure()
    plt.plot(x_plot, y_f, 'b-', label='Función original')
    plt.plot(x_plot, y_p, 'r--', label=f'Polinomio grado {g_degree}')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(f'Aproximación polinómica continua de grado {g_degree}')
    plt.legend()
    plt.grid(True)
    plt.show()

# Ejemplo 1: sin(x) con grado 2 en [0, 2]
print("\n--- Aproximación de sin(x) con polinomio de grado 2 en [0, 2] ---")
f1 = lambda x: np.sin(x)
aprox2(f1, 2, 0, 2)

# Ejemplo 2: cos(arctan(x)) - log(x+5) con grado 4 en [-2, 0]
print("\n--- Aproximación de cos(arctan(x)) - log10(x+5) con polinomio de grado 4 en [-2, 0] ---")
f2 = lambda x: np.cos(np.arctan(x)) - np.log10(x + 5)
aprox2(f2, 4, -2, 0)