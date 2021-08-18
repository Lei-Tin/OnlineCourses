# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 20:21:33 2021

@author: ray-h
"""

s = 'obboboobdboobncubboobbobobobbobob'

lowerBound = 0
upperBound = 3
numOfBob = 0

for i in range(len(s) - 2):
    
    if s[lowerBound:upperBound] == "bob":
        numOfBob += 1
    lowerBound += 1
    upperBound += 1
   
print("Number of times bob occurs is: " + str(numOfBob))