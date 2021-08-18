# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 23:08:06 2021

@author: ray-h
"""

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    
    output = []
    
    for i in secretWord:
        if i in lettersGuessed:
            output.append(i)
        else:
            output.append("_")
    
    return "".join(output)

secretWord = 'apple' 
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print(getGuessedWord(secretWord, lettersGuessed))