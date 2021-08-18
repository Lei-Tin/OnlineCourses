# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 20:27:28 2021

@author: ray-h
"""

# Find cube root

x = float(input("Number: "))

epsilon = 0.00000000000000000001
low = 0.0
high = x
numGuess = 0

guess = (low + high) / 2.0

while abs(guess ** 3 - x) >= epsilon:
    numGuess += 1
    
    if x > 0:
        if guess ** 3 > x:
            high = guess
        else:
            low = guess
            
    elif x < 0:
        if guess ** 3 > x:
            low = guess
        else:
            high = guess
    
    else: 
        guess = 0
        break
    
    guess = (low + high) / 2.0    

print("# of Guesses: " + str(numGuess))    
print("The cube root of that is: " + str(guess))