# -*- coding: utf-8 -*-
"""
Created on Mon May 24 21:15:15 2021

@author: ray-h
"""

import random

a = ['r', 'r', 'r', 'r', 'g', 'g', 'g', 'g']

prob = 0
count = 0

i = 0

while True:
    i += 1
    
    a = ['r', 'r', 'r', 'r', 'g', 'g', 'g', 'g']
    
    combo = random.sample(a, k=3)
    
    if combo == ['r', 'r', 'r'] or combo == ['g', 'g', 'g']:
        count += 1

    prob = count / i

    print(prob)


# print(combo)