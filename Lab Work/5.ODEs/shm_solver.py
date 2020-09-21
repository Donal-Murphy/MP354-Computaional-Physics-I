# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 14:48:21 2019

@author: Donal Murphy [15399561]
"""

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def shmderiv(y,t):
    """
    Calculates the derivatives for simple harmonic motion for use in odeint
    y is an array containing the position (x) and its derivative (v).
    """
    dy = np.zeros(2)       #Array containing derivatives
    dy[0] = y[1]            #dx/dt = v
    dy[1] = -y[0]           #dv/dt = -x
    return dy
    #Return dy

# Script to solve ODE: set up limits and spacings
tmin =  0.0
tmax = 22.0
dt   =  0.2                     #Spacing
tol  = 1e-3                     #Relative tolerance
y0 = [1.0,0.0]                  #Initial values
t = np.arange(tmin,tmax,dt)     #Set up vector of t -values

y = odeint(shmderiv,y0,t,rtol=tol)

plt.plot(t,y[:,0],'bo-',label ='odeint solution')
plt.plot(t,np.cos(t),'g-',label='cos(t)')
plt.xlabel("t")
plt.ylabel("y(t)")
plt.legend()
plt.figure()
plt.plot(t,y[:,0]-np.cos(t))
plt.xlabel("t")
plt.ylabel("error")
