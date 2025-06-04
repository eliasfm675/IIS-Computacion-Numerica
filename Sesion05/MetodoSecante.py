# -*- coding: utf-8 -*-
"""
Created on Sun Mar  2 15:46:02 2025

@author: Elías
"""
import numpy as np
def secante(f, x1, x0, tol=1.e-8, maxiter=100):
    xant=x0
    xi=x1
    i=0
    while np.abs(xi-xant)>tol and i<maxiter:
        temp=xi
        xi= xi - (f(xi)*(xi-xant))/(f(xi)-f(xant))
        xant=temp
        i+=1
    return xi
f=lambda x: x**2 -5
x0=2
x1=2.5
print(secante(f, x1, x0))

       
        