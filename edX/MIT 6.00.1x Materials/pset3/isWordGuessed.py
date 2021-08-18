# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 22:55:28 2021

@author: ray-h
"""

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    
    secretWordCopy = secretWord[:]
    
    for i in secretWord:
        if i in lettersGuessed:
            secretWordCopy = secretWordCopy.replace(i, "")
    
    if secretWordCopy == "":
        return True
    else: 
        return False

    
secretWord = 'apple' 
lettersGuessed = ['a', 'p', 'l', 'e', 'd', 's']
print(isWordGuessed(secretWord, lettersGuessed))