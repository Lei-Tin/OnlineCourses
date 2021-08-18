# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 16:44:32 2021

@author: ray-h
"""

def cipher(map_from, map_to, code):
    """ map_from, map_to: strings where each contain 
                          N unique lowercase letters. 
        code: string (assume it only contains letters also in map_from)
        Returns a tuple of (key_code, decoded).
        key_code is a dictionary with N keys mapping str to str where 
        each key is a letter in map_from at index i and the corresponding 
        value is the letter in map_to at index i. 
        decoded is a string that contains the decoded version 
        of code using the key_code mapping. """
        
    key_code = {}
    
    N = len(map_from)
    
    for i in range(N):
        key_code[map_from[i]] = map_to[i]
        
    # print(key_code)
        
    decodedList = []
    
    for i in code:
        decodedList.append(i)
    
    # print(decodedList)
    
    for i in range(len(decodedList)):
        decodedList[i] = key_code[decodedList[i]]
    
    # print(decodedList)
    
    decoded = "".join(decodedList)
    
    return (key_code, decoded)
    
    
print(cipher('abcd', 'dcba', 'dab'))