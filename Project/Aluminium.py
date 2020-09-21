# -*- coding: utf-8 -*-
"""
Created on Thu May  9 15:22:52 2019

@author: Donal Murphy

Description:
"""

import numpy as np # Required for exponential functions and arrays
from scipy.integrate import odeint # Required to calculate the radial function
import matplotlib.pyplot as plt # Required for plotting 

def shoot(r,E):
    """
    Shooting method for finding eigenvalues
    """

    def R_der(R,r):
        """
        Calculates the derivatives of R
        """
        
        Z = 13  # Atomic number of aluminium
        V = (-2/r)*((Z-1)*(1+(1.5*r/2))*np.exp(-1.5*r)+1) # Potential
        l = 1   # Angular momentum quantum number
        
        dR = np.zeros(2)    # Buffer for R derivative
        dR[0] = R[1]        # dy/dx = v
        # Equation for the radial function
        dR[1] = V*R[0]+(l*(l+1)/r**2)*R[0]-(2/r)*R[1]-E*R[0]
        
        return dR
    
    
        
    
    R_i = 0     # We know that at r = 0, the radial function is zero
    dR_i = 1    # For odd function
        
    R = odeint(R_der,[R_i, dR_i],r) # Solve
    
    return R 

rmin = 0.01
rmax = 10
dr = 0.01
r = np.arange(rmin,rmax+dr,dr)

E1,E2 = 0.7,10  # range to shoot

itermax = 1000
prec = 1e-6

# Bisection method
iter = 0
while ( abs(E1-E2) > prec ) and (iter < itermax):
    E3 = (E1+E2)/2.0
    R_array = shoot(r,E3)
    R = R_array[-1,0]
    if (R > 0):
        E2 = E3;
    else:
        E1 = E3;       
    iter += 1;

print('{0:.5f}'.format(E1))

# plot solution
plt.plot(r,R_array[:,0])
plt.title('2p Energy level',fontsize=20,color='r')
plt.xlabel(r'$r(a_0)$', fontsize = 15)
plt.ylabel('$R(r)$', fontsize = 15)
plt.grid(True)
plt.savefig('2p(2).png',bbox_inches = "tight")
#plt.legend();
plt.show()