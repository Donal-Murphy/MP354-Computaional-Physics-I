# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 15:13:06 2019

@author: Donal Murphy [15399561]
"""

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

GM = 58.9639


def kepler_eqs(y,t):
    dy = np.zeros(4)
    dy[0] = y[1]
    dy[1] = y[0]*(y[3]**2) - GM/(y[0]**2)
    dy[2] = y[3]
    dy[3] = -2*((y[1]*y[3])/y[0])
    return dy
    
def run_kepler(r0,v0,th0,w0,tmax):
    dt = 0.01
    t = np.arange(0,tmax+dt,dt)
    y0 = [r0,v0,th0,w0]
    y = odeint(kepler_eqs,y0,t)
    return t,y
    
tmax = 4.0
r0 = 1.05
v0 = 0.0
th0 = 0.0
w0 = np.sqrt(GM) - 0.1

t,y = run_kepler(r0,v0,th0,w0,tmax)

plt.figure(1)
plt.plot(t,y[:,0],label="$r(t)$")
plt.plot(t,y[:,1],label=r'$v_r(t)$')
plt.plot(t,y[:,2],label=r'\theta(t)$')
plt.plot(t,y[:,3],label=r'$\dot{theta}(t)$')
plt.xlabel("t")
plt.ylabel("y(t)")
plt.legend()
plt.savefig('kepler.png')

#polar plot
plt.figure(2)
plt.polar(y[:,2],y[:,0])
plt.show()
