# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 15:07:13 2019

Exercise 3) use a for loop to calculate the sum of 2n From n = 1-100

@author: donalm95
"""

import numpy as np

A = np.arange(1,101)

N = 0

for n in A:
    N = N + 2*n

print(N)
