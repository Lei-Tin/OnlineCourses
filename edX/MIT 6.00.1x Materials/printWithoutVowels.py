# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 16:05:25 2021

@author: ray-h
"""

def print_without_vowels(s):
    '''
    s: the string to convert
    Finds a version of s without vowels and whose characters appear in the 
    same order they appear in s. Prints this version of s.
    Does not return anything
    '''
    
    sNoVol = s[:]    
    
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    
    for i in vowels:
        sNoVol = sNoVol.replace(i, '')
    
    print(sNoVol)
    
    # Your code here
    
mystring = 'abcdefghijklmnopqrstuvwxyzaaa, bbb, eeeiii,,uuu'

print_without_vowels(mystring)