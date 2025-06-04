# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 16:32:11 2025

@author: uo299673
"""

import numpy as np
import matplotlib as mt
np.set_printoptions(precision=1,suppress=True)#usar para que no se usen ni exponentes ni (precision)
A=np.array([(2,1,3,4),(9,8,5,7),(6,-1,-2,-8),(-5,-7,-9,-6)])
print("A:")
print(A)
print("a:")
print(A[:,0]) #así cojo columnas, de la primera en este caso

print("b:")
print(A[2])

print("c:")
print(A[0:2,0:2]) #primer parámetro 0:2 indica que FILAS coge(de la 0 a la 2(no incluido)) y el segundo parametro de 0:2 indica las columnas
  
print("d:")
print(A[2:,2:])

print("e:")
print(A[1:3,1:3])

print("f:")
print(A[0:,1:])

print("g:")
print(A[1:,1:-1])