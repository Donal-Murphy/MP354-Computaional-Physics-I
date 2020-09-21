# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 14:04:52 2019

@author: Donal Murphy [15399561]
"""
import numpy as np

def function(x):
    return (x**3)-5
    
def midpoint(x1,x2):
    return (x1+x2)/2.0

x1=0.0
x2=2
error=1.0
n=1

while error >= 1e-6:
    
    for i in range(0,n):
        
        
            z= midpoint(x1,x2)
            
            if function(z) < 0:
                x1=z
            else:
                x2=z
            
            error = abs(x1-x2)
    n=n+1

print '{0:.6f}'.format(x1)