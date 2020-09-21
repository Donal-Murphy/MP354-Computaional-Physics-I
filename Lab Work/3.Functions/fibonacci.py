# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 14:11:02 2019

@author: Donal Murphy [15399561]
"""

#create a fuction for fibonacci series
def fibonacci(n):
    
    if (n<1):
        print('Error: illegal input value n<1')
        return
    
    if (type(n) is not int):
        print('Error: Non-integer value of n')
        return
        
    f = [1]*n   #creates an list n elements long
        
    for i in range (2,n):
        f[i] = f[i-2] + f[i-1]   #for entry i, add the previous 2 entries
    return f    #f only exists inside the definition (local variable)
                    #it can't be called on anywhere else in the program
