# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 16:09:35 2025

@author: UO299673
"""

import numpy as np
import time 
np.set_printoptions(suppress = True) # no usar notación exponencial
def multiplicar_1bucle(A,B):
    m, n = A.shape
    o, p = B.shape
    o=n
    C = np.zeros((m,p))
    suma=0
    for j in range(p):
         C[:,j]=np.sum(A*B[:,j], axis=1)      
    return C

def multiplicar_2bucles(A,B):
    m, n = A.shape
    o, p = B.shape
    o=n
    C = np.zeros((m,p))
    suma=0
    for i in range(m):
        for j in range(p):
            C[i,j]=np.sum(A[i,:]*B[:,j])

        
    return C
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


m = 300; n = 200; p = 400
A = np.random.rand(m,n)
B = np.random.rand(n,p)
print("Tiempo de ejecución con tres bucles")
t= time.time()
multiplicar_3bucles(A, B)
t1=time.time()
print(t1-t)
print("Tiempo de ejecución con dos bucles")
t= time.time()
C = multiplicar_2bucles(A, B)
t2=time.time()
print(t2-t)
print("Tiempo de ejecución con un bucle")
t= time.time()
multiplicar_1bucle(A, B)
t3=time.time()
print(t3-t)
print("Tiempo de ejecución con np.dot")
t= time.time()
np.dot(A, B)
t4=time.time()
print(t4-t)
print("Tiempo de ejecución con @")
t= time.time()
A@B
t5=time.time()
print(t5-t)




