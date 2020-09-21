# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 14:49:32 2019

@author: Donal Murphy [15399561]
"""

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def pendulum_der(y,t):
    """
    Calculates derivatives for a simple pendulum for use in odeint. y is an 
    array containing its position(x) and its derivative (v).
    """
    dy = np.zeros(2)
    dy[0] = y[1]
    dy[1] = -np.sin(y[0])
    return dy
    
tmin = 0.0
tmax = 60.0
dt = 0.1
tol = 1e-2
y0 = [1.0,0.0]
t = np.arange(tmin,tmax,dt)

y = odeint(pendulum_der,y0,t,rtol=tol)

plt.plot(t,y[:,0],'bo-',label ='odeint solution')
plt.plot(t,np.sin(t),'g-',label='sin(t)')
plt.xlabel("t")
plt.ylabel("y(t)")
plt.legend()
plt.figure()
plt.plot(t,y[:,0]-np.sin(t))
plt.xlabel("t")
plt.ylabel("error")
    