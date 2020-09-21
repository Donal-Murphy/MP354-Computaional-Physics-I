# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 15:01:24 2019

@author: Donal Murphy [15399561]
"""

import numpy as np
import math

n = input('n: ')
lam = input('lambda: ')

def poisson(n,lam):
    """
    calculates poisson distribution
    n must be non-negative integer
    lam (lambda) must be positive
    """
    
    #test for valid input
    if type(n) is not int:
        print('Error: n must be an integer')
        return      #return with no value
    if (n<0):
        print('Error: n must be non-negative')
        return
    if (lam<=0):
        print('Error: lambda must be positive')
        return
    else:
        return lam**n*np.exp(-lam)/math.factorial(n)
        
#test function
print(poisson(n,lam))

        