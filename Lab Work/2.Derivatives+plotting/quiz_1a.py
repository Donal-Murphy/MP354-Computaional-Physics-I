# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 14:35:00 2019

Class test 1, lab 3, quiz 1a

@author: Donal Murphy [15399561]
"""
# import libraries
import matplotlib.pyplot as plt
import numpy as np

delta = 0.001
E = np.arange(0.2,0.8,delta) # define the variable
r = (np.exp(-1.0/E))*(np.sin(1.0/(4.0*(E**3.0)))) # define the function

# find the number of elements the array has
N = len(E)

# create an array for derivative
dr = np.zeros(N)

#calculate the backwards derivative
for i in range(N-1):
    dr[i] = (r[i+1] - r[i])/delta
    
dr[-1] = dr[-2]
    
# plot the funtion
plt.plot(E,r)
plt.title('Graph of $r(\\xi) = e^{-1/\\xi}\sin(1/4\\xi^3$)') # plot title
plt.xlabel('$\\xi$'), plt.ylabel('$r(\\xi)$') # label axes
plt.show() # display graph
plt.savefig('graph_q1a.png') # save graph as png

#plot the derivative
plt.figure() # create a new graph
plt.plot(E,dr)
plt.title('Backwards Derivative of $r(\\xi)$')
plt.xlabel('$\\xi$'), plt.ylabel('$dr/d\\xi$')
plt.savefig('derivative_q1a.png')
plt.show