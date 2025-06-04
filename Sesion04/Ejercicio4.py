# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 16:09:35 2025

@author: UO299673
"""

import numpy as np
np.set_printoptions(precision = 2)   # solo dos decimales
np.set_printoptions(suppress = True) # no usar notación exponencial
def multiplicar_3bucles(A,B):
    m, n = A.shape
    o, p = B.shape
    o=n
    C = np.zeros((m,p))
    suma=0
    for k in range(n):
        for i in range(m):
            for j in range(p):
                C[i,j]+=A[i][k]*B[k][j]

        
    return C


A = np.array([[-3.,2],[-2,0],[-4,4],[4,-4]])
B = np.array([[4.,-3,1],[-2,1,1]])
print(multiplicar_3bucles(A, B), "\n")
