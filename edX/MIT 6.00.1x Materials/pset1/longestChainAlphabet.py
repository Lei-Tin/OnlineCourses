# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 22:00:05 2021

@author: ray-h
"""

s = 'xjrvskulgltgaxml'

Longest = ""
currLongest = ""

lowerBound = 0
upperBound = 1

for index in range(len(s)):
        
    if index < len(s) - 1: 
        if s[index] <= s[index + 1]:
            currLongest = s[lowerBound:upperBound]
            upperBound += 1
        
        elif s[index] > s[index + 1]:
            currLongest = s[lowerBound:upperBound]
            lowerBound = index + 1
            upperBound = index + 2
    
    
    # print("Index: " + str(index))
    # print(currLongest)
    # print(lowerBound)
    # print(upperBound)
    
        
    if len(currLongest) > len(Longest):
        Longest = currLongest
        
    currLongest = s[lowerBound:upperBound]
    
    if len(currLongest) > len(Longest):
        Longest = currLongest
        
print("Longest substring in alphabetical order is: " + Longest)