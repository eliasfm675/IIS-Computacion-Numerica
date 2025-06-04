# -*- coding: utf-8 -*-
"""
Created on Sun Mar  2 15:46:02 2025

@author: Elías
"""
import numpy as np
def regulaFalsi(f, a, b, tol=1.e-8, maxiter=100):
    error=np.inf
    b0=b
    a0=a
    i=0
    while np.abs(error)>tol and i<maxiter:
        m=(a*f(b)-b*f(a))/(f(b)-f(a))
        if f(a)*f(m)<0:
            b=m
        else:
            a=m
        i+=1
        error=(b0-a0)/2**i
    return m
  
    
f=lambda x: x**2 -9
x0=2
x1=5
print(regulaFalsi(f, x1, x0))

       
        