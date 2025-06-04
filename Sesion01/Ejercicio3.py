# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 16:15:47 2025

@author: uo299673
"""

import numpy as np
import matplotlib as mt
np.set_printoptions(precision=1,suppress=True)#usar para que no se usen ni exponentes ni (precision)
print("V:")
v=np.arange(0., 12.2, 1.1)
print(v)


print("Vi:")
vi=v[::-1]
print(vi)


print("V1:")
v1=v[::2]
print(v1)


print("V2:")
v2=v[1::2]
print(v2)

print("V1-1:")
v11=v[::3]
print(v11)

print("V2-1:")
v21=v[1::3]
print(v21)

print("V3-1:")
v31=v[2::3]
print(v31)

print("V1-2:")
v12=v[::4]
print(v12)

print("V2-2:")
v22=v[1::4]
print(v22)

print("V3-2:")
v32=v[2::4]
print(v32)


print("V4:")
v42=v[3::4]
print(v42)