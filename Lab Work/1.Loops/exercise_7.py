# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 16:04:04 2019

write out a script which prints out all numbers from 1 to 100
but if the number is a multiple of 5 print out the word 'fizz' instead
and if the number is a multiple of 7 print out the word 'buzz' instead
and if its a multiple of 5 & 7 print out 'fizzbuzz'

@author: donalm95
"""
import numpy as np

A = np.arange(1,101)

for n in A:
    
    if n % 5 == 0 and n % 7 == 0:
        print('fizzbuzz')
    
    elif n % 5 == 0:
        print('fizz')
    
    elif n % 7 == 0:
        print('buzz')
        
    else:
        print(n)
    
    
