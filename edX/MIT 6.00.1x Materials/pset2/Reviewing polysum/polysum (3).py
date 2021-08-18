# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 13:47:23 2021

@author: Ray
"""

# Math module is imported as it is needed for tan() and value of pi
import math

def polysum(n, s):
    """
    Parameters
    ----------
    n : Integers
        Number of sides of a polygon
        Any integer will work
        
    s : Integers or Floats
        Length of each side in a polygon
        Any number or float will work

    Returns
    -------
    Sum of the Area of the polygon and Perimeter of the polygon squared
    i.e. A + P ^ 2
    Where: 
        A = Area of polygon
        P = Perimeter of polygon
    """
        
    # Finding the Area
    # math.tan() is the tangent function
    # math.pi gives the approximate value of pi
    Area = (0.25 * n * (s ** 2) / (math.tan(math.pi / n)))
    
    # Finding the Perimeter
    # Number of sides times the length is the Perimeter
    Perimeter = n * s
    
    # Rounds the answers to 4 decimal places using round(a, b)
    # Where: 
        # a is the original value
        # b is the decimal places you want
    # Returns the rounded value
    return round(Area + Perimeter ** 2, 4)
