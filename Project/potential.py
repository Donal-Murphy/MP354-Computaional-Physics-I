# -*- coding: utf-8 -*-
"""
Created on Fri May 10 03:37:56 2019

@author: Donal Murphy

Description: Plots a graph of the potential
"""
import numpy as np # Required for exponential functions and arrays
import matplotlib.pyplot as plt # Required for plotting

Z = 13    # Atomic number of aluminium
r = np.arange(0,10,0.1)   # radial distance
V = (-2/(-r))*((Z-1)*(1+((1.5*(-r)/2))*np.exp(-1.5*(-r))+1)) # model for the potential

# Plot a graph
plt.plot(r,V,label='V')
plt.title('Potential Model',fontsize=20,color='r')
plt.xlabel(r'$r$',fontsize=14)
plt.ylabel('$V(r)$',fontsize=14)
plt.legend()
plt.grid(True)
plt.savefig('Potential.png',bbox_inches = "tight")
plt.show()
