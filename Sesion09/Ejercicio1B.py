
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 31 15:31:33 2025

@author: UO299673
"""
import numpy as np
import matplotlib.pyplot as plt
import sympy as sym
def dibujo(f,a,b,nodos):
    x=np.linspace(a, b,100)
    p=np.polyfit(nodos,f(nodos),len(nodos)-1)
    xp=np.linspace(a, b)
    yp=np.polyval(p,xp)
    pa=np.polyval(p,a)
    pb=np.polyval(p,b)
    plt.figure()
    plt.plot(x,0*x,'k')
    plt.plot(x,f(x), label='Área exacta')
    plt.plot([a,a,b,b],[f(a),0,0,f(b)],'b')
    plt.plot(nodos,f(nodos),'ro', label='Puntos de interpolación')
    plt.plot(xp,yp,'r--', label='Área aproximada')
    plt.plot([a,a,b,b],[pa,0,0,pb],'r--')
    plt.legend()
    plt.show()
def trapecio(f,a,b):
    xm=(b-a)/2
    I =xm*(f(a)+f(b))
    return I
f=lambda x: np.log(x)
x=np.linspace(a:=1, b:=3,100)
I=trapecio(f, a, b)
i=(a+b)/2
nodos=np.array([a,b])
dibujo(f,a,b,nodos)

x=sym.Symbol('x',real=True)
f_sim=sym.log(x)
I_exacta=sym.integrate(f_sim,(x,1,3))
print("El valor aproximado es ",I)
print("El valor exacto es ", float(I_exacta))