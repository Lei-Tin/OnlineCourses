# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 21:57:49 2021

@author: ray-h
"""

def is_even(i):
    """
    Input i, the number to be tested if even or not
    Returns true if i is even, false otherwise
    """
    
    return i % 2 == 0

x = int(input("Number: "))

if is_even(x) == True:
    print(f"{x} is even")
else:
    print(f"{x} is not even")
    
