# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 14:54:16 2019

@author: Donal Murphy [15399561]
"""

def sumfn(x,N):
    tot = 0.0;
    for n in range(1,N+1):
        tot += (1-x)**n/n
        
    return tot
    
#test function
print sumfn(1.2,10)