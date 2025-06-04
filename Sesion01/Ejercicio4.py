# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 23:33:17 2025

@author: Elías
"""

import numpy as np
import matplotlib.pyplot as plt
np.set_printoptions(precision=2,suppress=True)
a=np.array([1,2,3])
a=np.append(0, a)
a=a[::-1]
a=np.append(0., a)
print("First form:")
print(a)



b=np.array([0.,0,0,0,0])
a=np.array([1,2,3])
b[1]=a[0]
b[2]=a[1]
b[3]=a[2]
print("Second form:")
print(b)


c=np.array([0])
a=np.array([1.,2,3])
c=np.concatenate((c,a), axis=None)
c=np.append(0, c[::-1])
c=c[::-1]
print("Third form:")
print(c)
