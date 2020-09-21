# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 15:31:31 2019

pick values for a,b
use an if statement to print out maximum of {a,b}

@author: donalm95
"""

a = float(input('Enter a value for a: '))
b = float(input('Enter a value for b: '))

if a >= b:
    print('max{a,b} = '+ str(a))

else:
    print('max{a,b} = '+ str(b))