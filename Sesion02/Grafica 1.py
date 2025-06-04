# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import matplotlib.pyplot as plt
import time
f = lambda x: np.exp(x)
a = -1.;b=1 #[a,b]
x = np.linspace(a, b, 5)
y=f(x)
Ox=0*x
plt.figure()
plt.plot(x,y, label = "f")
plt.plot(x, Ox, label="Eje Ox")
plt.title("Ejemplo dibujo función f")
plt.legend()
plt.show()
