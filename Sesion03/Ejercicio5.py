import numpy as np
import numpy.polynomial.polynomial as pol 
np.set_printoptions(suppress = True)

def horner(x0,p):
    n=len(p)
    q=np.zeros(n)
    q[-1]=p[-1]
    for i in range(n-2,-1,-1):
        q[i]=p[i]+q[i+1]*x0
    cociente=q[1:]
    resto=q[0]
    return cociente, resto
def divisores(n):
    n=np.abs(int(n))
    div=[]
    for i in range(1, n+1):
        if n%i==0:
            div.append(i)
            div.append(-i)
    return np.array(div)
def raices(p):
    n=len(p)
    poli=np.copy(p)
    div = divisores(p[0])
    roots=[]
    for i in range(len(div)):
        poli=np.copy(p)
        for j in range(len(div)):
            c, r = horner(div[i], poli)
            if r==0:
                roots.append(div[i])
                poli=c
    return np.array(roots)
    
        
p0 = np.array([-1,0,1])
p1 = np.array([8., -22, 17, 1, -5, 1])
p2 = np.array([-135., 378, -369, 140, -9, -6, 1])
p3 = np.array([96., 320, 366, 135, -30, -24, 0, 1]) 
p4 = np.array([280., 156, -350, -59, 148, -26, -6, 1])
print("Raíces de p0")
print(raices(p0))
print("Raíces de p1")
print(raices(p1))
print("Raíces de p2")
print(raices(p2))
print("Raíces de p3")
print(raices(p3))
print("Raíces de p4")
print(raices(p4))