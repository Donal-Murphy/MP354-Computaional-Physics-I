# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 15:52:56 2019

@author: donalm95
"""

a = float(input('Enter a value for a: '))
b = float(input('Enter a value for b: '))
c = float(input('Enter a value for c: '))

if a>=b and a>=c:
    print('max{a,b,c} = '+ str(a))
    
elif a<b and b>=c:
    print('max{a,b,c} = '+ str(b))
    
else:
    print('max{a,b,c} = '+ str(c))
    