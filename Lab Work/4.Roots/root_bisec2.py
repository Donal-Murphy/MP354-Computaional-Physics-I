# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 14:55:28 2019

@author: Donal Murphy [15399561]
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2,2,100)
y = np.log((x*x)+1.0)/(x+2.0)-(x**3.0)*(1.0+(np.cos(x)))-1.0
plt.plot(x,y)
plt.plot(x,np.zeros(100))
plt.show()


def function(x):
    return np.log((x*x)+1.0)/(x+2.0)-(x**3.0)*(1.0+(np.cos(x)))-1.0
    
def midpoint(x1,x2):
    return (x1+x2)/2.0

x1=0.0
x2=-1
error=1.0
n=1

while error >= 1e-8:
    
    for i in range(0,n):
        
        
            z= midpoint(x1,x2)
            
            if function(z) < 0:
                x1=z
            else:
                x2=z
            
            error = abs(x1-x2)
    n=n+1

print ('root = ' +str(x1))
print ('error = '+str(error))