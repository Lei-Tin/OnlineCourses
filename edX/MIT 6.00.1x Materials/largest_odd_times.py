# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 16:16:40 2021

@author: ray-h
"""

def largest_odd_times(L):
    """ Assumes L is a non-empty list of ints
        Returns the largest element of L that occurs an odd number 
        of times in L. If no such element exists, returns None """
        
      
    myDict = {}
    
    for i in L:
        myDict[i] = myDict.get(i, 0) + 1
            
    myDictCpy = myDict.copy()
    
    for i in myDictCpy:
        if myDict[i] % 2 != 1:
            myDict.pop(i)
        
            
    maximum = 0
    for i in myDict:
        if i > maximum:
            maximum = i
    
    # print(maximum)
    if maximum != 0:
        return maximum
    else:
        return None
    
    # Your code here
    
L = [3, 9, 5, 3, 5, 3]
Y = [2, 2, 4, 4]

print(largest_odd_times(Y))