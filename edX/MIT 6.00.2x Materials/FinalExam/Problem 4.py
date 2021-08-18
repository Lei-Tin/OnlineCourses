# -*- coding: utf-8 -*-
"""
Created on Mon May 24 21:43:52 2021

@author: ray-h
"""
import random, pylab

# You are given this function
def getMeanAndStd(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    std = (tot/len(X))**0.5
    return mean, std

# You are given this class
class Die(object):
    def __init__(self, valList):
        """ valList is not empty """
        self.possibleVals = valList[:]
    def roll(self):
        return random.choice(self.possibleVals)

# Implement this -- Coding Part 1 of 2
def makeHistogram(values, numBins, xLabel, yLabel, title=None):
    """
      - values, a sequence of numbers
      - numBins, a positive int
      - xLabel, yLabel, title, are strings
      - Produces a histogram of values with numBins bins and the indicated labels
        for the x and y axis
      - If title is provided by caller, puts that title on the figure and otherwise
        does not title the figure
    """

    pylab.hist(values, numBins)
    
    if title != None:    
        pylab.title(title)
        
    pylab.xlabel(xLabel)
    pylab.ylabel(yLabel)
    pylab.show()
    
                    
# Implement this -- Coding Part 2 of 2
def getAverage(die, numRolls, numTrials):
    """
      - die, a Die
      - numRolls, numTrials, are positive ints
      - Calculates the expected mean value of the longest run of a number
        over numTrials runs of numRolls rolls.
      - Calls makeHistogram to produce a histogram of the longest runs for all
        the trials. There should be 10 bins in the histogram
      - Choose appropriate labels for the x and y axes.
      - Returns the mean calculated
    """
    longestList = []
    
    for i in range(numTrials):
        combo = []
        
        for j in range(numRolls):
            combo.append(die.roll())
        
        # print(combo)
        run = 1
        currLongest = 1
        for idx in range(len(combo) - 1):
            if combo[idx] == combo[idx + 1]:
                run += 1
                if run > currLongest:
                    currLongest = run
            
            else:
                run = 1
                
        # print(currLongest)
        longestList.append(currLongest)
        
    makeHistogram(longestList, 10, "1", "2")
    
    return sum(longestList) / len(longestList)

# print(getAverage(Die([1,2,3,4,5,6]), 5, 5))

# One test case
print(getAverage(Die([1,2,3,4,5,6,6,6,7]), 500, 10000))