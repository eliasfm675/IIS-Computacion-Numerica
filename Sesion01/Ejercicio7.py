import numpy as np
import matplotlib.pyplot as plt
np.set_printoptions(precision=2,suppress=True)
f=lambda x : x*np.sin(3*x) #-2pi 2pi cerrado
x=np.linspace(-2*np.pi, 2*np.pi)
Ox = 0*x
plt.figure()
plt.plot(x, f(x))
plt.plot(x,Ox, 'k-')
plt.xlabel("x")
plt.ylabel("y")
plt.title("x*sen(3x)")
plt.show()