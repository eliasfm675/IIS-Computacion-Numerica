# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 15:30:09 2025

@author: uo299673
"""


import numpy as np
import matplotlib.pyplot as plt
import numpy.polynomial.polynomial as pol
np.set_printoptions(suppress = True)
def horner(x0, p):
    n = len(p)
    q = np.zeros(n)
    q[-1] = p[-1]
    for i in range(n-2, -1, -1):
        q[i]=q[i+1]*x0+p[i]
    cociente = q[1:]
    resto = q[0]
    return cociente, resto
def dersucA(x0,p):
    n=len(p)
    derivada=np.zeros_like(p)
    factorial=1
    P=p
    for i in range(n):
        P, derivada[i] = horner(x0,P)
    return derivada
def dersucB(x0,p):
    n=len(p)
    derivada=np.zeros_like(p)
    factorial=1
    P=p
    for i in range(n):
        P, derivada[i] = horner(x0,P)
        derivada[i]*=factorial
        factorial*=i+1
    return derivada
        
    
p = np.array([1., -1, 2, -3,  5, -2])
x0 = 1.

r = np.array([1., -1, -1, 1, -1, 0, -1, 1])
x1 = -1.
print("Apartado A")
print("Restos de dividir P una y tra vez por (x-x0)")
print(dersucA(x0,p))

print("Restos de dividir R una y otra vez por (x-x1)")
print(dersucA(x1,r))

print("Apartado B")
print("Derivadas sucesivas de P en x0 = 1")
print(dersucB(x0, p))
print("Derivadas sucesivas de R en x1 = -1")
print(dersucB(x1, r))