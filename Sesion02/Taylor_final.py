import numpy as np
import matplotlib.pyplot as plt

#%%--------------------------------------
def P(x0,grado):
    polinomio = 0.
    factorial = 1.

    for i in range(grado+1):
        sumando = x0**i/factorial
        polinomio += sumando
        factorial *= i+1

    return polinomio 

#%%--------------------------------------

f = lambda x: np.exp(x)
a = -3.; b = 3.
x = np.linspace(a,b)
y = f(x)

OX = 0*x                               

plt.figure()

plt.plot(x,y, label = 'f')
plt.plot(x,OX,'k') 

for grado in range(1,7):
    plt.plot(x,P(x,grado), label = 'P'+str(grado))
    plt.title('Ejemplo dibujo de la función y los polinomios') 
    plt.legend()   
    plt.pause(1) 

plt.show()