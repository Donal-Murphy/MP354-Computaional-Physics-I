# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 15:19:16 2019

@author: Donal Murphy [15399561]
"""

import numpy as np

while True:
    
    x = input('Enter x (-pi < x < pi): ')
    N = input('Enter integer N: ')

    def sumsin(x,N):
        """
        calculates sum[n=1 to N](sin^n(x)/2n^2)
        N must be a positive integer >=1
        x must be between -pi and +pi
        """
        #test for valid input
        if type(N) is not int:
            print('Error: N must be an integer')
            return      #return with no value
        if (x < -np.pi) or (x > np.pi):
            print('Error: x must be in [-pi,pi]')
            return
    
        sinx = np.sin(x)        #calculate only once
        f = 0.0                 #initialise sum to 0
        for n in range(1,N+1):  #sum up terms from 1 to N
            f += (sinx**n)/(2*n**2)
            
        return f

    #print function        
    print sumsin(x,N)