# -*- coding: utf-8 -*-
"""
Created on Mon Mar 31 15:55:31 2025

@author: UO299673
"""
import numpy as np
import matplotlib.pyplot as plt
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
    plt.plot(nodos,f(nodos),'ro', label='Área aproximada')
    plt.plot(xp,yp,'r--', label='Área aproximada')
    plt.plot([a,a,b,b],[pa,0,0,pb],'r--')
    plt.legend()
    plt.show()
f1=lambda x: np.exp(x)
f2=lambda x: np.cos(x)+1.5
nodos1=np.array([1,2,2.5])
nodos2=np.array([-3.,-1,0,1,3])
dibujo(f1,0,3,nodos1)
dibujo(f2,-3,3,nodos2)

    