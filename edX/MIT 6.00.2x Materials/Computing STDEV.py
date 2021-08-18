# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 15:09:27 2021

@author: ray-h
"""
import math

# Calculating STDEV
data = [10, 4, 12, 15, 20, 5]

def getSTDEV(L):
    # Returns the STDEV of the list L, which contains only numbers
    
    X = []
    
    for i in L:
        X.append((i - (sum(L)/len(L)))**2)
        
    return math.sqrt(sum(X)/len(L))

print(getSTDEV(data))

print(round(getSTDEV(data)/(sum(data)/len(data)),3))