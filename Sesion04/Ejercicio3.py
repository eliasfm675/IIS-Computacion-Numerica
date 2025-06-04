import numpy as np

np.set_printoptions(precision=2, suppress=True)  # Configurar la visualización de números

def triangulariza_tridiagonal(Ar, b):
    n = len(b)
    At = np.copy(Ar)
    bt = np.copy(b)
    
    for k in range(n - 1):
        f = At[k + 1, 0] / At[k, 1]  # Factor de eliminación
        At[k + 1, 0] = 0.0
        At[k + 1, 1] -= f * At[k, 2]  # Modificar diagonal principal
        bt[k + 1] -= f * bt[k]  # Modificar vector b
    
    return At, bt

def sust_rev_tridiagonal(At, bt):
    n = len(bt)
    x = np.zeros(n)
    x[n - 1] = bt[n - 1] / At[n - 1, 1]  # Última variable
    
    for k in range(n - 2, -1, -1):
        x[k] = (bt[k] - At[k, 2] * x[k + 1]) / At[k, 1]
    
    return x

# Datos de prueba para n = 7
n = 7
Ar = np.zeros((n, 3))
Ar[:, 0] = np.concatenate((np.array([0]), np.ones((n - 1),)))
Ar[:, 1] = np.ones((n,)) * 3
Ar[:, 2] = np.concatenate((np.ones((n - 1),), np.array([0])))
b = np.arange(n, 2 * n) * 1.0

At, bt = triangulariza_tridiagonal(Ar, b)
print("Ar")
print(Ar)
print("b")
print(b)
print("x")
print(sust_rev_tridiagonal(At, bt))

# Datos de prueba para n = 8
n = 8
np.random.seed(3)
Ar = np.zeros((n, 3))
Ar[:, 1] = np.random.rand(n)
Ar[:, 0] = np.concatenate((np.array([0]), np.random.rand(n - 1)))
Ar[0:n - 1, 2] = Ar[1:n, 0]
b = np.random.rand(n)

At, bt = triangulariza_tridiagonal(Ar, b)
print("x'")
print(sust_rev_tridiagonal(At, bt))
