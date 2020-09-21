# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 14:38:30 2019

@author: Donal Murphy [15399561]
"""

import numpy as np
import matplotlib.pyplot as plt

 
a = 0
b = 30
dx = 0.1
y_0 = -1/2

while (dx>=0.001):   
    x = np.arange(a,b+dx,dx)
    N = len(x)
    y = np.zeros(N)
    y[0] = y_0
    
    for i in range(N-1):
        y[i+1] = y[i] + dx*(np.cos(x[i])/(x[i]+1))
        
    plt.plot(x,y,label = 'Euler dx=' + str(dx))
    plt.title("Solution of y'(x)=cos(x)/(x+1)")
    plt.xlabel('x')
    plt.ylabel('y(x)')
    plt.legend()
    plt.show()
    
    dx *= 0.1