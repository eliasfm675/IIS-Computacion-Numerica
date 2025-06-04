# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 15:32:39 2025

@author: UO299673
"""

import numpy as np
np.set_printoptions(precision = 2)   # solo dos decimales
np.set_printoptions(suppress = True) # no usar notación exponencial
def triangulariza(A,b):
    n=len(b)
    At = np.copy(A)
    bt = np.copy(b)
    for k in range(n-1):
        f = At[k+1,k]/At[k,k]
        At[k+1,k]=0.
        At[k+1,k+1] -= f*At[k,k+1]
        bt[k+1] -= f*bt[k]
    return At, bt
def sust_rev(At, bt):
    n = len(bt)
    x = np.zeros(n)
    x[n-1]=bt[n-1]/At[n-1,n-1]
    for k in range(n-2, -1, -1):
        x[k] = (bt[k]-At[k,k+1]*x[k+1])/At[k,k]
    return x
n = 7 

A1 = np.diag(np.ones(n))*3
A2 = np.diag(np.ones(n-1),1) 
A = A1 + A2 + A2.T 
b = np.arange(n,2*n)*1.

print('A')
print(A)
print('b')
print(b)
print(np.linalg.solve(A,b))
             