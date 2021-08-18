# -*- coding: utf-8 -*-
"""
Created on Mon May 24 21:41:52 2021

@author: ray-h
"""

import random

def drawing_without_replacement_sim(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    4 red and 4 green balls. Balls are not replaced once
    drawn. Returns a float - the fraction of times 3 
    balls of the same color were drawn in the first 3 draws.
    '''
    # Your code here 
   
    ans = 0
    
    for i in range(numTrials):
        bucket = ['r', 'r', 'r', 'r', 'g', 'g', 'g', 'g']
        
        combo = random.sample(bucket, k = 3)
        
        if combo == ['r', 'r', 'r'] or combo == ['g', 'g', 'g']:
            ans += 1
            
    return float(ans / numTrials)