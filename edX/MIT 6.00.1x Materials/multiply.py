# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 10:14:31 2021

@author: ray-h
"""

def multiply(a, b):
    """
    Input: a and b as integers
    Output: the multiplication product of a and b
    """

    if b <= 1:
        return a
    else: 
        return a + multiply(a, b - 1)
    
ans = multiply(int(input("x: ")), int(input("y: ")))

print("x * y = " + str(ans))