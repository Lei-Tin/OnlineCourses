# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 14:54:02 2021

@author: ray-h
"""

def genPrimes():
    
    primeList = []
    
    x = 1
    
    while True:
        x += 1
        
        for i in primeList:
            if (x % i) == 0:
                break
            
        else:
            primeList.append(x)
            yield x