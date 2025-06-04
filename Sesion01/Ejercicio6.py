# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 16:45:56 2025

@author: uo299673
"""

import numpy as np
import matplotlib as mt
np.set_printoptions(precision=1,suppress=True)#usar para que no se usen ni exponentes ni (precision)
f= lambda x : x*np.exp(x)
print("f(x):")
print(f(2))

g= lambda z: z/(np.sin(z)*np.cos(z))
print("g(z):")
print(g(np.pi/4))

h=lambda x, y: (x*y)/(x**2+y**2)

print("h(x, y):")
print(h(2,4))