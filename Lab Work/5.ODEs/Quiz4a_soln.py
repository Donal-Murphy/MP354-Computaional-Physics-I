# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 14:09:14 2019

@author: Donal Murphy [15399561]
"""
"""
Initial value was estimated manually to be about 2
"""

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def y_der(y,x):
    Z = 13.0  # Atomic number of aluminium
    V = (-2.0/x)*((Z-1.0)*(1.0+(1.5*x/2.0))*np.exp(-1.5*x)+1.0)
    E = 1
    l = 1
    
    dy = np.zeros(2)
    dy[0] = y[1]        # dy/dx = v
    dy[1] = V*y[0]+(l*(l+1.0)/x**2.0)*y[0]-(2.0/x)*y[1]-E*y[0]
    return dy
    
def midpoint(x1,x2):
    return (x1+x2)/2.0
    
  
xmin = 1
xmax = 10
dx = 0.1
x = np.arange(xmin,xmax+dx,dx)

y_i = 1
v_i = 2


y = odeint(y_der,[y_i, v_i],x)


# plot solution
plt.plot(x,y[:,0])
plt.xlabel("x")
plt.ylabel("y(x)")
plt.savefig('shoot.png')
#plt.legend();
plt.show()
