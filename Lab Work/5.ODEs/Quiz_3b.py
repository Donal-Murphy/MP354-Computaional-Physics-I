# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 14:08:41 2019

@author: Donal Murphy [15399561]
"""

# Import necassary libraries
import numpy as np
import matplotlib.pyplot as plt

def euler(x,dx,J,dJ): 
   
   # Euler method
    for i in range(N-1):
        J[i+1] = J[i] + dx*(dJ[i]*(J[i]/2)+x[i]/2)
        dJ[i+1] = dJ[i] + dx*J[i]
"""
Calculates the solution to the ODE using the Euler method
"""

def plot(x_axis,y_axis):
    
    plt.plot(x_axis,y_axis,label = 'Euler dx=' + str(dx))
    plt.title(r"Solution to $\frac{d^{2}J}{dx^{2}}-\frac{x}{2}-" + 
    r"\frac{1}{2}(\frac{dJ}{dx})J=0$")
    plt.xlabel('x')
    plt.ylabel('J(x)')
    plt.legend()
    plt.show()
"""
Plots a graph
"""

# Initialize and declare variables/boundaries
x_i = 0     # Lower Range
x_f = 5     # Upper Range
dx = 0.001  # Step size
J_0 = -5    # Functon J(0)
dJ_0 = 2    #Function J'(0)

x = np.arange(x_i,x_f+dx,dx) # Array for values of x
N = len(x)                   # Length of array of x
    
J = np.zeros(N)     # Creates empty array J(x)
J[0] = J_0          # Fills first element with J(0)
dJ = np.zeros(N)    # Creates empty array J'(x)
dJ[0] = dJ_0        # Fills first element with J'(0)


euler(x,dx,J,dJ)    # Calls on function euler() 
plot(x,dJ)          # Plots a graph of results



    
