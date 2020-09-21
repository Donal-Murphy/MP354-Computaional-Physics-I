# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 13:59:11 2019

@author: Donal Murphy [15399561]
"""
#-----------------------------------------------------------------------------#
#function for the pareto distribution
def pareto(x,xm,alpha):
    """
    for pareto distribution, probability density:
    = 0 if x<=xm
    = (alpha*xm**alpha)/x**(alpha + 1) if x>xm
    """
    #if   xm <= 0) and/or (alpha <= 0):
    if (xm <= 0) and (alpha <= 0):   
        return 'Error: xm and alpha must be greater than 0.'
    
    if (xm <= 0):
        return 'Error: xm must be greater than 0.'
    
    if (alpha <= 0):
        return 'Error: alpha must be greater than 0.'
    
    #if xm and alpha are valid:
    if (x<= xm):    
        return 0
     
    else:   
        return((alpha*xm**alpha)/x**(alpha + 1))
#-----------------------------------------------------------------------------#
ans = 1
while (ans == 1):
    #initialize variables and ask for user input
    x = input('\nPlease enter a real number x: ')
    xm = input('\nPlease enter a positive real number xm: ')
    alpha = input('\nPlease enter a positive real number alpha: ')

        
#print the results
    print('\np('+str(x)+','+str(xm)+','+str(alpha)+') = '+\
    str(pareto(x,xm,alpha)))
    ans = input('\nEvaluate again? (1 = Yes, 2 = No): ')
    
if ans == 0:
    print('End')