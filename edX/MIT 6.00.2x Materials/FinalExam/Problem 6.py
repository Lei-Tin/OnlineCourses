# -*- coding: utf-8 -*-
"""
Created on Mon May 24 22:04:33 2021

@author: ray-h
"""
import os
os.environ["OPENBLAS_NUM_THREADS"] = "1"
import numpy as np

def find_combination(choices, total):
    """
    choices: a non-empty list of ints
    total: a positive int
 
    Returns result, a numpy.array of length len(choices) 
    such that
        * each element of result is 0 or 1
        * sum(result*choices) == total
        * sum(result) is as small as possible
    In case of ties, returns any result that works.
    If there is no result that gives the exact total, 
    pick the one that gives sum(result*choices) closest 
    to total without going over.
    """
    
    ans = []
    
    complete = False
    
    if total in choices:
        for i in range(len(choices)):
            if choices[i] == total:
                if complete == False:
                    ans.append(1)
                        
                elif i == len(choices) - 1:
                    ans.append(0)
                else:
                    ans.append(0)
                    
                complete = True
            
            else: 
                ans.append(0)
                    
    if sum(choices) <= total:
        for i in range(len(choices)):
            ans.append(1)
        
    # Total is lesser than all numbers in the choices
    flag = True
    for i in range(len(choices)):
        if total >= choices[i]:
            flag = False
            break
            
        else:
            flag = True
                
    if flag == True:
        for i in range(len(choices)):            
            ans.append(0)
            
    return np.array(ans)
    
    
    
print(find_combination([1,3,4,2,5], 16))