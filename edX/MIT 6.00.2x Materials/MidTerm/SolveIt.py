# -*- coding: utf-8 -*-
"""
Created on Mon May  3 23:02:08 2021

@author: ray-h
"""

def solveit(test):
    """ test, a function that takes an int parameter and returns a Boolean
        Assumes there exists an int, x, such that test(x) is True
        Returns an int, x, with the smallest absolute value such that test(x) is True 
        In case of ties, return any one of them. 
    """
    # IMPLEMENT THIS FUNCTION
    
    x = 0
    while test(x) != True and test(-x) != True:
        x += 1
    
    if test(x) == True:
        return x
    
    elif test(-x) == True:
        return -x
    
    

#### This test case prints 49 ####
def f(x):
    return (x+15)**0.5 + x**0.5 == 15
print(solveit(f))

#### This test case prints 0 ####
def f(x):
    return x == 0
print(solveit(f))

def f(x):
    return x**2 + 2*x + 1 == 0
print(solveit(f))