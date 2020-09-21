# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 15:11:32 2019

Exercise 4) Pick a value for x
            Use a for loop to calculate:
            (Sigma n= 0-50)[(-1)^n . x^(2n+1)]/(2n+1)!
            
            compare this value with sin(x)

@author: donalm95
"""
import numpy as np
 
A = np.arange(0,51)
 
N = 0
 
x = float(input('enter any value for x: '))

 
for n in A:
     N = N + (((-1)**n) * x**(2*n + 1)) / np.math.factorial(2*n + 1)
     
print(N)