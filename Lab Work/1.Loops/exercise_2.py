# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 14:32:12 2019

Ex. 2) Use a for loop to print out all odd numbers from 1 to 100

@author: donalm95
"""
# import numby for array
import numpy as np

# Create an array from 1 - 100
A = np.arange(1,101)

# print numbers from 1 - 100
for n in A:
    if n % 2 != 0:
        print(n)