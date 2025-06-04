import numpy as np
import matplotlib.pyplot as plt
import numpy.polynomial.polynomial as pol

def chebyshev(f, a, b, n):
    # Nodos equiespaciados
    xe = np.linspace(a, b, n)
    ye = f(xe)
    
    # Nodos de Chebyshev
    i = np.arange(1, n + 1)
    xc = np.cos((2 * i - 1) * np.pi / (2 * n))  # En [-1,1]
    yc = f(xc)
    
    # Puntos para graficar
    xx = np.linspace(a, b, 500)
    yy = f(xx)
    
    # Polinomios interpolantes
    pe = pol.polyfit(xe, ye, n - 1)
    pc = pol.polyfit(xc, yc, n - 1)
    
    # Graficar interpolación con nodos equiespaciados
    plt.figure()
    plt.plot(xx, yy, 'b', label='Función real')
    plt.plot(xx, pol.polyval(xx, pe), 'r', label='Interpolación')
    plt.scatter(xe, ye, color='red', label='Nodos Equiespaciados')
    plt.title('Nodos Equiespaciados')
    plt.axis([-1.05, 1.05, -0.3, 2.3])
    plt.legend()
    plt.show()
    
    # Graficar interpolación con nodos de Chebyshev
    plt.figure()
    plt.plot(xx, yy, 'b', label='Función real')
    plt.plot(xx, pol.polyval(xx, pc), 'r', label='Interpolación')
    plt.scatter(xc, yc, color='red', label='Nodos Chebyshev')
    plt.title('Nodos de Chebyshev')
    plt.axis([-1.05, 1.05, -0.3, 2.3])
    plt.legend()
    plt.show()

# Definir funciones
f1 = lambda x: 1 / (1 + 25 * x**2)
f2 = lambda x: np.exp(-20 * x**2)

a, b, n = -1, 1, 11
chebyshev(f1, a, b, n)
chebyshev(f2,a,b,n)