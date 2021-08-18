# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 23:12:47 2021

@author: ray-h
"""

import string

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    
    letters = string.ascii_lowercase
    
    for i in lettersGuessed:
        if i in string.ascii_lowercase:
            letters = letters.replace(i, "")
            
    return letters

lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print(getAvailableLetters(lettersGuessed))